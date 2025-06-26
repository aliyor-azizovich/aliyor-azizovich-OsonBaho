# from PyQt5.QtWidgets import QDialog, QPushButton, QTextBrowser, QCheckBox, QLabel
# from PyQt5 import uic
# from PyQt5.QtCore import Qt
# import os
# from logic.data_entry import DataEntryForm

# class RentDialog(QDialog):
#     def __init__(self, parent=None, data_service=None):
#         super().__init__(parent)
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "rent_dialog.ui"), self)

#         self.data_service = data_service or DataEntryForm()
#         self.df_rent_2025 = self.data_service.load_rent_2025()

#         # Привязка элементов интерфейса
#         self.pushButton_rent_ok = self.findChild(QPushButton, "pushButton_rent_ok")
#         self.textBrowser_gov_rent = self.findChild(QTextBrowser, "textBrowser_gov_rent")
#         self.textBrowser_market_rent = self.findChild(QTextBrowser, "textBrowser_market_rent")
#         self.checkBox_gov_rent = self.findChild(QCheckBox, "checkBox_gov_rent")
#         self.checkBox_market_rent = self.findChild(QCheckBox, "checkBox_market_rent")
#         self.label_gov_rent = self.findChild(QLabel, "label_gov_rent")

#         self.checkboxes = [self.checkBox_gov_rent, self.checkBox_market_rent]
#         BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
#         self.project_dir = BASE_DIR
#         self.pushButton_rent_ok.clicked.connect(self.accept)
#         for cb in self.checkboxes:
#             cb.stateChanged.connect(self.single_selection)

#         explanation_text = (
#             "В соответствии с установленными ставками минимальной арендной платы на 2025 год,\n"
#             "расчет производится с учетом повышающих коэффициентов, определяемых местными органами власти.\n"
#             "Эти коэффициенты варьируются в зависимости от уровня социально-экономического развития районов и городов.\n"
#             "Программа автоматически определяет регион и устанавливает соответствующую ставку."
#         )
#         self.textBrowser_gov_rent.setText(explanation_text)


#         # Путь к изображению
#         image_path = os.path.join(self.project_dir, "icon", "rent_region.png")
#         if os.path.exists(image_path):
#             html_image = f'<img src="{image_path}" width="500">'
#             self.textBrowser_market_rent.setHtml(html_image)
#         else:
#             self.textBrowser_market_rent.setText("Изображение не найдено.")

#     def set_text_and_checkbox(self, region_name: str):
#         """Устанавливает значение арендной ставки по региону"""
#         if self.df_rent_2025.empty:
#             self.label_gov_rent.setText("Данные о ставках отсутствуют.")
#             self.checkBox_gov_rent.setText("Нет данных")
#             return

#         df = self.df_rent_2025.copy()
#         df["Region"] = df["Region"].str.strip()

#         row = df[df["Region"] == region_name.strip()]
#         if not row.empty:
#             rent_value = row["rent_2025"].values[0]
#             self.checkBox_gov_rent.setText(f"{rent_value:,.2f} сум/м.кв.")
#             self.checkBox_gov_rent.setProperty("raw_value", rent_value)  # 👈 сохраняем чистое число
#             self.label_gov_rent.setText(f"Минимальная арендная ставка по региону: {region_name}")
#         else:
#             self.checkBox_gov_rent.setText("Нет данных")
#             self.label_gov_rent.setText(f"Ставка не найдена для региона: {region_name}")

#     def get_selected_rent_type(self):
#         if self.checkBox_gov_rent.isChecked():
#             return self.checkBox_gov_rent.property("raw_value")  # 👈 получаем float
#         elif self.checkBox_market_rent.isChecked():
#             return 25000  # например, рыночная ставка по умолчанию
#         return None

#     def single_selection(self):
#         """Разрешает выбрать только один чекбокс"""
#         sender = self.sender()
#         for cb in self.checkboxes:
#             if cb != sender:
#                 cb.setChecked(False)


    