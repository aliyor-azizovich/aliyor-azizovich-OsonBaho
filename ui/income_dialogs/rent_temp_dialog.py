# from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel, QCheckBox
# from PyQt5 import uic
# from PyQt5.QtCore import Qt
# import os
# import requests
# from logic.data_entry import DataEntryForm
# from PyQt5.QtGui import QPixmap

# class RentTempDialog(QDialog):
#     def __init__(self, parent=None, data_service=None):
#         super().__init__(parent)
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "rent_temp_dialog.ui"), self)
#         self.data_service = data_service or DataEntryForm()
#         # поднимаемся на два уровня от rent_temp_dialog.py
#         BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
#         self.project_dir = BASE_DIR
        


#         # Привязка всех QLineEdit
       
#         self.pushButton_renttemp_ok = self.findChild(QPushButton, "pushButton_renttemp_ok")
#         self.pushButton_renttemp_ok.clicked.connect(self.accept)

#         self.label_title = self.findChild(QLabel, "label_title")
#         self.label_rent_chart = self.findChild(QLabel, "label_rent_chart")
#         self.checkBox_mean_temp = self.findChild(QCheckBox, "checkBox_mean_temp")
#         self.checkBox_mean_temp.clicked.connect(self.single_selection)
#         self.checkBox_median_temp = self.findChild(QCheckBox, "checkBox_median_temp")
#         self.checkBox_median_temp.clicked.connect(self.single_selection)
#         self.checkBox_lastyear_temp = self.findChild(QCheckBox, "checkBox_lastyear_temp")        
#         self.checkBox_lastyear_temp.clicked.connect(self.single_selection)
#         self.checkboxes = [self.checkBox_mean_temp, self.checkBox_median_temp, self.checkBox_lastyear_temp]
        
#     from PyQt5.QtGui import QPixmap

#     def set_labels_and_chart(self, oblast_name: str, rayon_name: str):
#         if self.df_rent_temp is None or self.df_rent_temp.empty:
#             self.label_title.setText("Нет данных по арендным ставкам.")
#             return

#         # Удаляем лишние пробелы в названиях столбцов (на всякий случай)
#         df = self.df_rent_temp.copy()
#         df.columns = df.columns.str.strip()

#         region = None
#         if oblast_name == "город Ташкент":
#             region = "Ташкент"
#             self.label_title.setText(
#                 "Темп роста минимальных арендных ставок по городу Ташкент за 2021-2025 г. \n"
#                 "согласно установленным ставкам в Законе «О Государственном бюджете Республики Узбекистан (2021г.-2025г.)"
#             )
#             chart_filename = "Ташкент.png"

#         elif "город" in rayon_name.lower():
#             region = "Областные центры"
#             self.label_title.setText(
#                 "Темп роста минимальных арендных ставок по г. Нукус, и областных центров за 2021-2025 г. \n"
#                 "согласно установленным ставкам в Законе «О Государственном бюджете Республики Узбекистан (2021г.-2025г.)"
#             )
#             chart_filename = "Областные центры.png"

#         else:
#             region = "Районы"
#             self.label_title.setText(
#                 "Темп роста минимальных арендных ставок по районам за 2021-2025 г. \n"
#                 "согласно установленным ставкам в Законе «О Государственном бюджете Республики Узбекистан (2021г.-2025г.)"
#             )
#             chart_filename = "Районы.png"

#         # Путь к изображению
#         # base_path = os.path.dirname(os.path.abspath(__file__))
#         icon_path = os.path.join(self.project_dir, "icon", chart_filename)
#         if os.path.exists(icon_path):
#             self.label_rent_chart.setPixmap(QPixmap(icon_path))
#             self.label_rent_chart.setScaledContents(True)
       

#         # Извлекаем значения темпов из таблицы
#         row = df[df["Населённый пункт"].str.strip() == region]
#         if not row.empty:
#             self.checkBox_mean_temp.setText(f"Средний темп - {row['Средний темп (%)'].values[0]}%")
#             self.checkBox_median_temp.setText(f"Медианный темп - {row['Медианный темп (%)'].values[0]}%")
#             self.checkBox_lastyear_temp.setText(f"Темп за последний год - {row['Темп за последний год (%)'].values[0]}%")
#         pixmap = QPixmap(icon_path)
#         if not pixmap.isNull():
           
#             self.label_rent_chart.setPixmap(pixmap)
#             self.label_rent_chart.setScaledContents(True)
#         else:
#             print("❌ QPixmap пустой — возможно, проблема с кодировкой файла или форматом")


#     def get_selected_temp_value(self):
#         if self.checkBox_mean_temp.isChecked():
#             return "Средний темп", self.checkBox_mean_temp.text().split("-")[-1].strip()
#         elif self.checkBox_median_temp.isChecked():
#             return "Медианный темп", self.checkBox_median_temp.text().split("-")[-1].strip()
#         elif self.checkBox_lastyear_temp.isChecked():
#             return "Темп роста за последний год", self.checkBox_lastyear_temp.text().split("-")[-1].strip()
#         return "", ""


#     def single_selection(self):
#         """Выбор только одного чекбокса"""
#         sender = self.sender()
#         for cb in self.checkboxes:
#             if cb != sender:
#                 cb.setChecked(False)