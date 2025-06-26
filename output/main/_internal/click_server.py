from flask import Flask, request, jsonify
from license_updater import update_valid_until

app = Flask(__name__)

@app.route("/click/complete", methods=["POST"])
def click_complete():
    transaction_param = request.form.get("merchant_trans_id") or request.form.get("merchant_prepare_id")

    if not transaction_param:
        return jsonify({"error": -5, "error_note": "Отсутствует transaction_param"})

    try:
        period, client_id = transaction_param.split("_", 1)
    except:
        return jsonify({"error": -6, "error_note": "Неверный формат transaction_param"})

    success = update_valid_until(client_id, period)

    if success:
        return jsonify({"error": 0, "error_note": "OK"})
    else:
        return jsonify({"error": -7, "error_note": "Клиент не найден"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
