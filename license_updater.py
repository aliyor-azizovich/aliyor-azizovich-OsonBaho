import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# Настройка доступа один раз при импорте
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("osonbaholicensing-b9bf7d3e1b19.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1BkfdRE2ZIVXRmigefS4J0K5IsmZyBqjpDuCjU-qHZTA").sheet1

def update_valid_until(client_id, period="month"):
    """
    Обновляет дату подписки для заданного client_id
    """
    try:
        data = sheet.get_all_records()
        for i, row in enumerate(data):
            if row.get("client_id") == client_id:
                if period == "day":
                    new_date = datetime.now() + timedelta(days=1)
                elif period == "month":
                    new_date = datetime.now() + timedelta(days=30)
                elif period == "year":
                    new_date = datetime.now() + timedelta(days=365)
                else:
                    new_date = datetime.now()

                sheet.update_cell(i + 2, list(row.keys()).index("valid_until") + 1, new_date.strftime("%Y-%m-%d"))
                print(f"[OK] Подписка {client_id} продлена до {new_date.strftime('%Y-%m-%d')}")
                return True

        print(f"[WARN] Пользователь {client_id} не найден.")
        return False

    except Exception as e:
        print(f"[ERROR] Ошибка обновления подписки: {e}")
        return False

def update_valid_until_partial(partial_client_id, period="month"):
        """
        Обновляет дату подписки для client_id, начинающегося с partial_client_id
        """
        try:
            data = sheet.get_all_records()
            for i, row in enumerate(data):
                full_id = row.get("client_id", "")
                if full_id.startswith(partial_client_id):  # сравниваем начало
                    if period == "day":
                        new_date = datetime.now() + timedelta(days=1)
                    elif period == "month":
                        new_date = datetime.now() + timedelta(days=30)
                    elif period == "year":
                        new_date = datetime.now() + timedelta(days=365)
                    else:
                        new_date = datetime.now()

                    sheet.update_cell(i + 2, list(row.keys()).index("valid_until") + 1, new_date.strftime("%Y-%m-%d"))
                    print(f"[OK] Подписка {full_id} продлена до {new_date.strftime('%Y-%m-%d')}")
                    return True

            print(f"[WARN] Пользователь, начинающийся с {partial_client_id}, не найден.")
            return False

        except Exception as e:
            print(f"[ERROR] Ошибка обновления подписки: {e}")
            return False
        
def _update_date(i, row, period):
    if period == "day":
        new_date = datetime.now() + timedelta(days=1)
    elif period == "month":
        new_date = datetime.now() + timedelta(days=30)
    elif period == "year":
        new_date = datetime.now() + timedelta(days=365)
    else:
        new_date = datetime.now()

    sheet.update_cell(i + 2, list(row.keys()).index("valid_until") + 1, new_date.strftime("%Y-%m-%d"))
    print(f"[OK] Подписка {row.get('client_id')} продлена до {new_date.strftime('%Y-%m-%d')}")
    return True    