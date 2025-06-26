import json
import urllib.request
from datetime import datetime
import os
import uuid
import urllib.parse
import socket
import hashlib
import subprocess
from pathlib import Path
from cryptography.fernet import Fernet
import base64
import csv
import io

LICENSE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQgHKRi9wHqyN8KdKekS5AI-DTH1ikZFyMKHK46Cn6MtAq91AR7xur2oNI2Krkl-vt47rY014flC25S/pub?gid=0&single=true&output=csv"
LOCAL_CACHE_FILE = "data/license_cache.json"


def get_secure_client_file():
    appdata = os.getenv("LOCALAPPDATA") or os.path.expanduser("~/.local/share")
    path = Path(appdata) / "OsonBaho" / ".license"
    path.mkdir(parents=True, exist_ok=True)
    return path / "client_id.json"


def get_disk_serial():
    try:
        if os.name == 'nt':
            output = subprocess.check_output("wmic diskdrive get SerialNumber", shell=True)
            return output.decode().split('\n')[1].strip()
        else:
            return "unknown"
    except:
        return "unknown"


def generate_strong_client_id():
    mac = uuid.getnode()
    hostname = socket.gethostname()
    disk_serial = get_disk_serial()
    base_str = f"{mac}-{hostname}-{disk_serial}"
    return hashlib.sha256(base_str.encode()).hexdigest()


def generate_encryption_key_from_hardware():
    mac = uuid.getnode()
    hostname = socket.gethostname()
    serial = get_disk_serial()
    base = f"{mac}-{hostname}-{serial}"
    key_raw = hashlib.sha256(base.encode()).digest()
    return base64.urlsafe_b64encode(key_raw[:32])



def get_public_id(client_id: str) -> str:
    """
    Генерация короткого безопасного ID для поддержки на основе client_id
    Пример: OB-1E79-AF97-F519
    """
    short = client_id[:12].upper()  # первые 12 символов SHA256
    part1 = short[:4]
    part2 = short[4:8]
    part3 = short[8:12]
    return f"OB-{part1}-{part2}-{part3}"


def get_client_id():
    client_file = get_secure_client_file()
    key_file = client_file.parent / "key.txt"

    if not key_file.exists():
        # Сгенерируем и сохраним ключ
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    else:
        key = key_file.read_bytes()

    fernet = Fernet(key)

    if not client_file.exists():
        client_id = generate_strong_client_id()
        encrypted_id = fernet.encrypt(client_id.encode())
        with open(client_file, "wb") as f:
            f.write(encrypted_id)
        send_client_id_to_admin(client_id)
        return client_id

    try:
        encrypted_id = client_file.read_bytes()
        return fernet.decrypt(encrypted_id).decode()
    except Exception as e:
        print(f"[ERROR] Ошибка расшифровки client_id: {e}")
        return None





def load_license_list():
    try:
        with urllib.request.urlopen(LICENSE_URL, timeout=5) as response:
            data = response.read().decode("utf-8")
            f = io.StringIO(data)
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print(f"[WARN] Не удалось загрузить лицензии: {e}")
        return []



def is_license_valid():
    client_id = get_client_id()
    if not client_id:
        return False

    licenses = load_license_list()
    for record in licenses:
        if record.get("client_id") == client_id:
            valid_until = record.get("valid_until")
            try:
                return datetime.strptime(valid_until, "%Y-%m-%d") >= datetime.now()
            except:
                return False
    return False


TELEGRAM_BOT_TOKEN = "7725822982:AAHoP7ZoPt0lBojODUmuEwl1GKKi-kRszOs"
ADMIN_CHAT_ID = 97346543

def send_client_id_to_admin(client_id):
    public_id = get_public_id(client_id)
    message = (
        "🆕 Новый пользователь\n"
        f"Public ID (для поддержки): {public_id}\n"
        f"Client ID (внутренний): {client_id}"
    )
    encoded_message = urllib.parse.quote(message)
    url = (
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        f"?chat_id={ADMIN_CHAT_ID}&text={encoded_message}"
    )
    try:
        with urllib.request.urlopen(url) as response:
            print(f"[INFO] Статус: {response.status}")
            print("[INFO] client_id и public_id отправлены в Telegram.")
    except Exception as e:
        print(f"[ERROR] Ошибка при отправке в Telegram: {e}")

