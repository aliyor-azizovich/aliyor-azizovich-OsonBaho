# from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton
# from PyQt5 import uic
# from PyQt5.QtCore import Qt
# import os
# import requests

# class DiscountDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "discount_dialog.ui"), self)

#         # Привязка всех QLineEdit
#         self.lineEdit_market_risk = self.findChild(QLineEdit, "lineEdit_market_risk")
#         self.lineEdit_segment_risk = self.findChild(QLineEdit, "lineEdit_segment_risk")
#         self.lineEdit_sales_period = self.findChild(QLineEdit, "lineEdit_sales_period")
#         self.lineEdit_liquidity = self.findChild(QLineEdit, "lineEdit_liquidity")
#         self.lineEdit_individual_risk = self.findChild(QLineEdit, "lineEdit_individual_risk")
#         self.lineEdit_risk_free = self.findChild(QLineEdit, "lineEdit_risk_free")
#         self.lineEdit_discount_rate = self.findChild(QLineEdit, "lineEdit_discount_rate")

#         self.pushButton_ok = self.findChild(QPushButton, "pushButton_ok")
#         self.pushButton_ok.clicked.connect(self.accept)

#         self.lineEdit_discount_rate.setReadOnly(True)
#         self.lineEdit_liquidity.setReadOnly(True)
#         self.lineEdit_risk_free.setReadOnly(True)
#         # Значения по умолчанию
#         self.lineEdit_market_risk.setText("2%")
#         self.lineEdit_segment_risk.setText("3%")
#         self.lineEdit_sales_period.setText("6 месяцев")
#         self.lineEdit_individual_risk.setText("2%")

#         # Получаем безрисковую ставку с сайта ЦБ РУз (временно — заглушка 14%)
#         try:
#             self.lineEdit_risk_free.setText("14%")
#         except:
#             self.lineEdit_risk_free.setText("14%")

#         # Обработка пользовательского ввода для добавления % и "месяц"
#         self.lineEdit_market_risk.editingFinished.connect(lambda: self.handle_input_change(self.lineEdit_market_risk))
#         self.lineEdit_segment_risk.editingFinished.connect(lambda: self.handle_input_change(self.lineEdit_segment_risk))
#         self.lineEdit_individual_risk.editingFinished.connect(lambda: self.handle_input_change(self.lineEdit_individual_risk))
#         self.lineEdit_sales_period.editingFinished.connect(self.handle_input_change)

#         # Инициализация первого расчёта при открытии окна
#         self.calculate_discount_rate()

#     def format_percent(self, line_edit):
#         text = line_edit.text().replace("%", "").strip()
#         if text:
#             try:
#                 val = float(text)
#                 line_edit.setText(f"{val:.2f} %")
#             except:
#                 line_edit.setText("0.00 %")

#     def format_months(self):
#         text = self.lineEdit_sales_period.text().lower()
#         number = ''.join(c for c in text if c.isdigit())
#         if number:
#             self.lineEdit_sales_period.setText(f"{number} месяцев")
#         else:
#             self.lineEdit_sales_period.setText("0 месяцев")

#     def handle_input_change(self, *args):
#         self.format_percent(self.lineEdit_market_risk)
#         self.format_percent(self.lineEdit_segment_risk)
#         self.format_percent(self.lineEdit_individual_risk)
#         self.format_months()
#         self.calculate_discount_rate()

#     def calculate_discount_rate(self):
#         try:
#             r_market = float(self.lineEdit_market_risk.text().replace("%", "").strip())
#             r_segment = float(self.lineEdit_segment_risk.text().replace("%", "").strip())
#             r_individual = float(self.lineEdit_individual_risk.text().replace("%", "").strip())
#             r_free = float(self.lineEdit_risk_free.text().replace("%", "").strip())
#             months = int(''.join(c for c in self.lineEdit_sales_period.text() if c.isdigit()))

#             r_liquidity = r_free * months / 12
#             r_total = r_market + r_segment + r_individual + r_free + r_liquidity

#             self.lineEdit_liquidity.setText(f"{r_liquidity:.2f} %")
#             self.lineEdit_discount_rate.setText(f"{r_total:.2f} %")

#         except Exception as e:
#             self.lineEdit_discount_rate.setText("Ошибка")
#     def keyPressEvent(self, event):
#         if event.key() in (Qt.Key_Up, Qt.Key_Down):
#             fields = [
#                 self.lineEdit_market_risk,
#                 self.lineEdit_segment_risk,
#                 self.lineEdit_sales_period,
#                 self.lineEdit_individual_risk
#             ]
#             current = self.focusWidget()
#             if current in fields:
#                 i = fields.index(current)
#                 if event.key() == Qt.Key_Down and i < len(fields) - 1:
#                     fields[i + 1].setFocus()
#                 elif event.key() == Qt.Key_Up and i > 0:
#                     fields[i - 1].setFocus()
