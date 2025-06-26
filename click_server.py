from flask import Flask, request, jsonify 
from license_updater import update_valid_until_partial
import logging
from logic.click_payment_checker import is_transaction_paid

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(
    filename='/opt/app/click.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

ERROR_CODES = {
    "SUCCESS": 0,
    "USER_NOT_FOUND": -5,
    "REQUEST_INVALID": -8
}

@app.route("/click/complete", methods=["POST"])
def click_complete():
    form = request.form.to_dict()
    logging.info("⤵️ Запрос от Click: %s", form)

    click_trans_id = form.get("click_trans_id")
    merchant_trans_raw = form.get("merchant_trans_id") or form.get("merchant_transs_id")
    merchant_prepare_id = form.get("merchant_prepare_id")

    if not merchant_trans_raw:
        return log_and_respond(click_trans_id, None, merchant_prepare_id,
                               ERROR_CODES["REQUEST_INVALID"], "Missing merchant_trans_id")

    merchant_trans_id = merchant_trans_raw

    try:
        period, partial_client_id = merchant_trans_raw.split("_", 1)
    except Exception as e:
        logging.error("❌ Ошибка разбора merchant_trans_id: %s", e)
        return log_and_respond(click_trans_id, merchant_trans_id, merchant_prepare_id,
                               ERROR_CODES["REQUEST_INVALID"], "Invalid merchant_trans_id format")

    logging.info("🔍 Попытка обновить подписку для partial_client_id=%s, period=%s",
             partial_client_id, period)

    # ✅ ДОБАВЛЕНО: проверка через Click API
    if not is_transaction_paid(click_trans_id):
        logging.warning("⛔ Оплата по click_trans_id=%s не подтверждена. Подписка НЕ продлена.", click_trans_id)
        return log_and_respond(click_trans_id, merchant_trans_id, merchant_prepare_id,
                           ERROR_CODES["USER_NOT_FOUND"], "Payment not confirmed")


    success = update_valid_until_partial(partial_client_id, period)

    if success:
        logging.info("✅ Подписка успешно продлена для partial_client_id=%s", partial_client_id)
        return log_and_respond(click_trans_id, merchant_trans_id, merchant_prepare_id,
                               ERROR_CODES["SUCCESS"], "Success")
    else:
        logging.warning("⚠️ Пользователь с partial_client_id=%s не найден", partial_client_id)
        return log_and_respond(click_trans_id, merchant_trans_id, merchant_prepare_id,
                               ERROR_CODES["USER_NOT_FOUND"], "User does not exist")

def log_and_respond(click_id, trans_id, prepare_id, error_code, note):
    response_data = {
        "click_trans_id": click_id,
        "merchant_trans_id": trans_id,
        "merchant_prepare_id": prepare_id,
        "error": error_code,
        "error_note": note
    }
    logging.info("↩️ Ответ сервером Click: %s", response_data)
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
