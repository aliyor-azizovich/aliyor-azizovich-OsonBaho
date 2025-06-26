import os
import pickle
from io import BytesIO
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha256
from logic.paths import get_data_pkg_path

class EncryptedDataLoader:
    def __init__(self, pkg_path='data.pkg', password=b'my-secret-password'):
        self.pkg_path = pkg_path or get_data_pkg_path()
        self.key = sha256(password).digest()
        self.iv = b'1234567890abcdef'  # должен совпадать с тем, что ты использовал при шифровании  
        self.data = {}

        self._load_and_decrypt()

    def _load_and_decrypt(self):
        if not os.path.exists(self.pkg_path):
            raise FileNotFoundError(f"{self.pkg_path} not found.")

        with open(self.pkg_path, 'rb') as f:
            encrypted = f.read()

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

        self.data = pickle.loads(decrypted)
        # print(f"[INFO] Загружено файлов: {len(self.data)}")

    def get(self, filename: str) -> BytesIO:
        if filename not in self.data:
            raise FileNotFoundError(f"{filename} not found in package.")
        return BytesIO(self.data[filename])

