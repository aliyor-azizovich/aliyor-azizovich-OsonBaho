import hashlib
import requests

# 🔐 Данные из Click (конфиденциальные — не публикуй в открытом виде)
MERCHANT_ID = '41279'
MERCHANT_USER_ID = '57615'
SECRET_KEY = 'yt43GtaTgSI8Y'

def is_transaction_paid(click_trans_id):
    """
    Проверяет, подтверждена ли транзакция в системе CLICK
    """
    sign_string = f"{MERCHANT_ID}{MERCHANT_USER_ID}{click_trans_id}{SECRET_KEY}"
    sign_hash = hashlib.md5(sign_string.encode('utf-8')).hexdigest()

    url = "https://api.click.uz/v2/merchant/transaction/status/"
    payload = {
        "click_trans_id": click_trans_id,
        "merchant_id": MERCHANT_ID,
        "merchant_user_id": MERCHANT_USER_ID,
        "sign_string": sign_hash
    }

    try:
        response = requests.post(url, data=payload, timeout=5)
        result = response.json()

        if result.get("error") == 0 and result.get("status") == "paid":
            print(f"[OK] Транзакция {click_trans_id} оплачена")
            return True
        else:
            print(f"[WARN] Транзакция {click_trans_id} НЕ оплачена: {result}")
            return False

    except Exception as e:
        print(f"[ERROR] Ошибка при проверке транзакции: {e}")
        return False
