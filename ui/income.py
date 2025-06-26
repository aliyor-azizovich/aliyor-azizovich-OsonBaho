# from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QTableWidget, QDialog, QTableWidgetItem, QComboBox
# from PyQt5.QtCore import Qt
# from PyQt5 import uic
# import os
# from ui.income_dialogs.discount_dialog import DiscountDialog
# from ui.income_dialogs.capitalization_dialog import CapitalizationDialog
# from ui.income_dialogs.tax_dialog import TaxDialog
# from ui.income_dialogs.rent_dialog import RentDialog
# from ui.income_dialogs.rent_temp_dialog import RentTempDialog
# from ui.income_dialogs.management_dialog import ManagementDialog
# from ui.income_dialogs.collect_losses_dialog import CollectLossesDialog
# from ui.income_dialogs.loading_losses_dialog import LoadingLossesDialog




# class IncomeWidget(QWidget):
#     def __init__(self, parent=None, main_window=None, valuation_window=None):
#         super().__init__(parent)
        
#         self.main_window = main_window
#         self.valuation_window = valuation_window
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "income_widget.ui"), self)
#         self.init_ui()
#         self.comboBox_rent_type.currentTextChanged.connect(self.update_income_living_area)
       


#     def init_ui(self):
#         # Здесь будут findChild подключения к элементам UI через объект .ui файла
#         # Пример:
#         self.pushButton_rent = self.findChild(QPushButton, "pushButton_rent")
#         self.pushButton_rent.clicked.connect(self.open_rent_dialog)
#         self.pushButton_income_ok = self.findChild(QPushButton, 'pushButton_income_ok')
#         self.pushButton_income_ok.clicked.connect(self.switch_to_comparative)

#         self.lineEdit_rent = self.findChild(QLineEdit, "lineEdit_rent")
#         # self.lineEdit_rent.setText("3 USD")

#         self.pushButton_temp_rent = self.findChild(QPushButton, "pushButton_temp_rent")
#         self.lineEdit_temp_rent = self.findChild(QLineEdit, "lineEdit_temp_rent")
#         self.lineEdit_temp_rent.setReadOnly(True)
#         self.label_temp = self.findChild(QLabel, "label_temp")

#         self.pushButton_temp_rent.clicked.connect(self.open_renttemp_dialog)


#         self.label_rent = self.findChild(QLabel, "label_rent")

#         # self.pushButton_vacancy = self.findChild(QPushButton, "pushButton_vacancy")
#         # self.lineEdit_vacancy = self.findChild(QLineEdit, "lineEdit_vacancy")

#         # self.pushButton_nonpayment = self.findChild(QPushButton, "pushButton_nonpayment")
#         # self.lineEdit_nonpayment = self.findChild(QLineEdit, "lineEdit_nonpayment")

#         self.pushButton_collect = self.findChild(QPushButton, "pushButton_collect")
#         self.pushButton_collect.clicked.connect(self.open_collect_losses_dialog)
        
#         self.lineEdit_collect = self.findChild(QLineEdit, "lineEdit_collect")
#         self.label_collect = self.findChild(QLabel, "label_collect")
#         self.lineEdit_collect.setReadOnly(True)
#         self.comboBox_rent_type = self.findChild(QComboBox, 'comboBox_rent_type')
        
#         self.pushButton_loading = self.findChild(QPushButton, "pushButton_loading")
#         self.pushButton_loading.clicked.connect(self.open_loading_losses_dialog)
        
#         self.lineEdit_loading = self.findChild(QLineEdit, "lineEdit_loading")
#         self.label_loading = self.findChild(QLabel, "label_loading")
#         self.lineEdit_loading.setReadOnly(True)


#         self.pushButton_management = self.findChild(QPushButton, "pushButton_management")
#         self.pushButton_management.clicked.connect(self.open_management_dialog)

#         self.lineEdit_management = self.findChild(QLineEdit, "lineEdit_management")
#         self.label_management = self.findChild(QLabel, "label_management")

#         self.pushButton_tax = self.findChild(QPushButton, "pushButton_tax")
#         self.lineEdit_tax = self.findChild(QLineEdit, "lineEdit_tax")

#         self.label_tax = self.findChild(QLabel, "label_tax")


#         self.pushButton_discount_rate = self.findChild(QPushButton, "pushButton_discount")
#         self.lineEdit_discount_rate = self.findChild(QLineEdit, "lineEdit_discount")
#         self.lineEdit_discount_rate.setReadOnly(True)

#         # self.pushButton_cap_rate = self.findChild(QPushButton, "pushButton_cap_rate")
#         # self.lineEdit_cap_rate = self.findChild(QLineEdit, "lineEdit_cap_rate")

#         self.pushButton_calculate = self.findChild(QPushButton, "pushButton_calculate")
#         self.pushButton_calculate.clicked.connect(self.calculate_income_valuation)

#         self.tableWidget_income_cost = self.findChild(QTableWidget, "tableWidget_income_cost")

#         self.lineEdit_DDP = self.findChild(QLineEdit, "lineEdit_DDP")
#         self.lineEdit_reversion = self.findChild(QLineEdit, "lineEdit_reversion")
#         self.lineEdit_income_cost = self.findChild(QLineEdit, "lineEdit_income_cost")
    

#         self.pushButton_tax.clicked.connect(self.update_tax_from_ukup)
#         self.pushButton_tax.clicked.connect(self.open_tax_dialog)

#         self.pushButton_discount_rate.clicked.connect(self.open_discount_dialog)
        
#         self.pushButton_capitalization = self.findChild(QPushButton, "pushButton_capitalization")
#         self.pushButton_capitalization.clicked.connect(self.open_capitalization_dialog)

#         self.lineEdit_capitalization = self.findChild(QLineEdit, "lineEdit_capitalization")
#         self.lineEdit_capitalization.setReadOnly(True)

#         self.lineEdit_living_area = self.findChild(QLineEdit, "lineEdit_living_area")
        

#         # self.lineEdit_living_area.setReadOnly(True)

#         rent_type = ['Площадь участка', 'Жилая площадь', 'Площадь застройки', 'Полезная площадь']
#         self.comboBox_rent_type.addItems(rent_type)
        

#         # self.update_income_living_area()

    

#     def update_income_living_area(self):
#         """Обновляет площадь в income_widget в зависимости от выбора в comboBox_rent_type."""

#         # Считываем тексты из главного окна
#         land_area = self.valuation_window.lineEdit_land_area.text()
#         living_area = self.valuation_window.lineEdit_living_area.text()
#         total_area = self.valuation_window.lineEdit_total_area.text()
#         usefull_area = self.valuation_window.lineEdit_useful_area.text()

#         # Смотрим выбранный вариант в комбобоксе
#         rent_type = self.comboBox_rent_type.currentText()

#         if rent_type == "Площадь участка":
#             self.lineEdit_living_area.setText(land_area)
#         elif rent_type == "Жилая площадь":
#             self.lineEdit_living_area.setText(living_area)
#         elif rent_type == "Площадь застройки":
#             self.lineEdit_living_area.setText(total_area)
#         elif rent_type == "Полезная площадь":
#             self.lineEdit_living_area.setText(usefull_area)
#         else:
#             # На всякий случай если ничего не выбрано
#             self.lineEdit_living_area.setText(land_area)



#     def update_tax_from_ukup(self):
#         try:
#             liter_table = self.valuation_window.ukup_tab.tableWidget_liter_list
#             last_row = liter_table.rowCount() - 1
#             if last_row < 0:
#                 raise ValueError("Таблица пуста")

#             item = liter_table.item(last_row, 4)
#             if not item:
#                 raise ValueError("Нет данных в итоговой строке")
#             text = item.text().replace(" ", "").replace(",", "")
#             total_valuated_cost = float(text)
#             self.building_price = total_valuated_cost

#             # Получаем площадь
#             area_text = self.valuation_window.lineEdit_living_area.text().replace(" ", "").replace(",", "")
#             area = float(area_text) if area_text else 0

#             # Получаем район из valuation_window
#             rayon_text = self.valuation_window.comboBox_rayon.currentText().lower()
#             oblast_text = self.valuation_window.comboBox_oblast.currentText().lower()

#             # Логика ставок
#             if area <= 200:
#                 tax_rate = 0.0034
#             elif "город" in rayon_text and area <= 500:
#                 tax_rate = 0.0045
#             elif ("город" in rayon_text or "город" in oblast_text) and area > 500:
#                 tax_rate = 0.006
#             elif "город" not in rayon_text and area > 200:
#                 tax_rate = 0.0045
#             else:
#                 tax_rate = 0.0034  # fallback

#             tax_amount = total_valuated_cost * tax_rate
#             self.label_tax.setText(f'{tax_rate*100:,.2f}% от стоимости улучшений')
#             tax_text = f"{tax_amount:,.2f}".replace(",", " ")
#             self.lineEdit_tax.setText(tax_text)
#             self.lineEdit_tax.setReadOnly(True)

#         except Exception as e:
#             print("")


#     def open_capitalization_dialog(self):
#         dialog = CapitalizationDialog(self)    
#         dialog.exec_()

#     def open_rent_dialog(self):
#         rayon = self.valuation_window.comboBox_rayon.currentText()
#         dialog = RentDialog(parent=self)
#         dialog.set_text_and_checkbox(rayon)

#         if dialog.exec_() == QDialog.Accepted:
#             selected_rent = dialog.get_selected_rent_type()
#             if selected_rent is not None:
#                 self.lineEdit_rent.setText(f"{selected_rent:.2f}")



#     def open_renttemp_dialog(self):
#         oblast = self.valuation_window.comboBox_oblast.currentText()
#         rayon = self.valuation_window.comboBox_rayon.currentText()

#         dialog = RentTempDialog(self)
#         dialog.df_rent_temp = dialog.data_service.rent_temp()
#         dialog.set_labels_and_chart(oblast_name=oblast, rayon_name=rayon)

#         if dialog.exec_() == QDialog.Accepted:
#             label_text, selected_value = dialog.get_selected_temp_value()
#             self.lineEdit_temp_rent.setText(selected_value)
#             self.label_temp.setText(label_text)
    
#     def open_management_dialog(self):
#         dialog = ManagementDialog(self)
#         if dialog.exec_() == QDialog.Accepted:
#             label, value = dialog.get_selected_management_risk()
#             # Преобразуем число в строку и устанавливаем в lineEdit
#             self.lineEdit_management.setText(f"{value * 100:.1f}%")
#             self.label_management.setText(f'{label}')


#     def open_collect_losses_dialog(self):
#         dialog = CollectLossesDialog(self)
#         if dialog.exec_() == QDialog.Accepted:
#             label, value = dialog.get_selected_collect_losses()
#             # Преобразуем число в строку и устанавливаем в lineEdit
#             self.lineEdit_collect.setText(f"{value * 100:.1f}%")
#             self.label_collect.setText(f'{label}')

#     def open_loading_losses_dialog(self):
#         dialog = LoadingLossesDialog(self)
#         if dialog.exec_() == QDialog.Accepted:
#             label, value = dialog.get_selected_loading_losses()
#             # Преобразуем число в строку и устанавливаем в lineEdit
#             self.lineEdit_loading.setText(f"{value * 100:.1f}%")
#             self.label_loading.setText(f'{label}')    


#     def calculate_discount_and_capitalization(self, discount_rate, individual_risk):
#         try:
#             discount = float(discount_rate)
#             individual = float(individual_risk)
#             capitalization = discount - individual

#             self.lineEdit_discount_rate.setText(f"{discount:.2f} %")
#             self.lineEdit_capitalization.setText(f"{capitalization:.2f} %")
#         except ValueError:
#             self.lineEdit_discount_rate.setText("Ошибка")
#             self.lineEdit_capitalization.setText("Ошибка")

    
#     def open_discount_dialog(self):
#         dialog = DiscountDialog(self)
#         if dialog.exec_() == QDialog.Accepted:
#             discount_text = dialog.lineEdit_discount_rate.text().replace("%", "").strip()
#             individual_text = dialog.lineEdit_individual_risk.text().replace("%", "").strip()
#             self.calculate_discount_and_capitalization(discount_text, individual_text)


#     def open_tax_dialog(self):
#         dialog = TaxDialog(self)
#         dialog.exec_()


#     def calculate_income_valuation(self):
        
#         try:
#             fields = [
#                 self.lineEdit_living_area.text(),
#                 self.lineEdit_rent.text(),
#                 self.lineEdit_temp_rent.text(),
#                 self.lineEdit_loading.text(),
#                 self.lineEdit_collect.text(),
#                 self.lineEdit_management.text(),
#                 self.lineEdit_tax.text(),
#                 self.lineEdit_discount_rate.text()
#             ]
#             if any(f.strip() == '' for f in fields):
#                 raise ValueError("Некоторые поля пусты")

#             def to_float(text):
#                 return float(''.join(c for c in text if c.isdigit() or c in ".,").replace(",", "."))

#             living_area = to_float(self.lineEdit_living_area.text())
#             rent = to_float(self.lineEdit_rent.text())
#             growth = to_float(self.lineEdit_temp_rent.text().replace("%", "")) / 100
#             loading = to_float(self.lineEdit_loading.text().replace("%", "")) / 100
#             collect = to_float(self.lineEdit_collect.text().replace("%", "")) / 100
#             management = to_float(self.lineEdit_management.text().replace("%", "")) / 100
#             tax = to_float(self.lineEdit_tax.text())
#             discount = to_float(self.lineEdit_discount_rate.text().replace("%", "")) / 100

#             tax_per_year = tax
#             annual_rent = living_area * rent * 12
#             previous_rent = annual_rent

#             self.tableWidget_income_cost.setRowCount(5)
#             self.tableWidget_income_cost.setColumnCount(5)
#             self.tableWidget_income_cost.setHorizontalHeaderLabels([
#                 "Год", "Годовая аренда", "Коэфф. дисконтирования", "ЧОД", "ДДП"
#             ])

#             for year in range(1, 6):
#                 if year == 1:
#                     rent_this_year = annual_rent
#                 else:
#                     rent_this_year = previous_rent * (1 + growth)

#                 noi = rent_this_year * (1 - (loading + collect + management)) - tax_per_year
#                 coeff = 1 / ((1 + discount) ** year)
#                 dcf = noi * coeff
                
#                  # Создание элементов таблицы
#                 year_item = QTableWidgetItem(f"{year} год")
#                 rent_item = QTableWidgetItem(f"{rent_this_year:,.2f}")
#                 coeff_item = QTableWidgetItem(f"{coeff:.6f}")
#                 noi_item = QTableWidgetItem(f"{noi:,.2f}")
#                 dcf_item = QTableWidgetItem(f"{dcf:,.2f}")

#                 # Установка флагов: только отображение, без редактирования
#                 for item in [year_item, rent_item, coeff_item, noi_item, dcf_item]:
#                     item.setFlags(item.flags() & ~Qt.ItemIsEditable)

#                 # Установка элементов в таблицу
#                 self.tableWidget_income_cost.setItem(year - 1, 0, year_item)
#                 self.tableWidget_income_cost.setItem(year - 1, 1, rent_item)
#                 self.tableWidget_income_cost.setItem(year - 1, 2, coeff_item)
#                 self.tableWidget_income_cost.setItem(year - 1, 3, noi_item)
#                 self.tableWidget_income_cost.setItem(year - 1, 4, dcf_item)
#                 previous_rent = rent_this_year
#             self.tableWidget_income_cost.resizeColumnsToContents()
#             self.tableWidget_income_cost.resizeRowsToContents()
#             self.tableWidget_income_cost.horizontalHeader().setStretchLastSection(True)
#             self.update_income_results()
#             self.valuation_window.save_report()
#         except Exception as e:
#             _ = e
#             pass
        
#     def update_income_results(self):
#         try:
#             row_count = self.tableWidget_income_cost.rowCount()
#             if row_count < 1:
#                 raise ValueError("Таблица доходов пуста")

#             # 1. Сумма всех значений из столбца "ДДП" (index 4)
#             dcf_total = 0.0
#             for row in range(row_count):
#                 item = self.tableWidget_income_cost.item(row, 4)
#                 if item is not None:
#                     value = float(item.text().replace(" ", "").replace(",", ""))
#                     dcf_total += value

#             self.lineEdit_DDP.setText(f"{dcf_total:,.2f}".replace(",", " "))

#             # 2. Расчёт Reversion
#             # ЧОД последнего года = столбец 3
#             noi_item = self.tableWidget_income_cost.item(row_count - 1, 3)
#             coeff_item = self.tableWidget_income_cost.item(row_count - 1, 2)
#             cap_rate_text = self.lineEdit_capitalization.text().replace("%", "").strip()

#             if noi_item is None or coeff_item is None or not cap_rate_text:
#                 raise ValueError("Недостаточно данных для расчёта реверсии")

#             noi = float(noi_item.text().replace(" ", "").replace(",", ""))
#             coeff = float(coeff_item.text())
#             cap_rate = float(cap_rate_text.replace(",", ".")) / 100

#             if cap_rate == 0:
#                 raise ZeroDivisionError("Коэффициент капитализации не может быть 0")

#             reversion = (noi / cap_rate) * coeff
#             self.lineEdit_reversion.setText(f"{reversion:,.2f}".replace(",", " "))

#             # 3. Итоговая стоимость
#             total_value = dcf_total + reversion
#             self.lineEdit_income_cost.setText(f"{total_value:,.2f}".replace(",", " "))
#             self.income_cost = total_value
#         except Exception as e:
#             print('')




#     # Сохраняем и загружаем обратно


#     def collect_income_data(self):
#         """Собирает все данные из вкладки доходного подхода для сохранения"""
#         data = {
#             "rent": self.lineEdit_rent.text(),
#             "label_rent": self.label_rent.text(),
#             "temp_rent": self.lineEdit_temp_rent.text(),
#             "label_temp": self.label_temp.text(),
#             # "vacancy": self.lineEdit_vacancy.text(),
#             # "nonpayment": self.lineEdit_nonpayment.text(),
#             "collect": self.lineEdit_collect.text(),
#             "label_collect": self.label_collect.text(),
#             "loading": self.lineEdit_loading.text(),
#             "label_loading": self.label_loading.text(),
#             "management": self.lineEdit_management.text(),
#             "label_management": self.label_management.text(),
#             "tax": self.lineEdit_tax.text(),
#             "label_tax": self.label_tax.text(),
#             "discount_rate": self.lineEdit_discount_rate.text(),
#             "capitalization": self.lineEdit_capitalization.text(),
#             # "cap_rate": self.lineEdit_cap_rate.text(),
#             "living_area": self.lineEdit_living_area.text(),
#             "rent_type": self.comboBox_rent_type.currentText(),
#             "ddp": self.lineEdit_DDP.text(),
#             "reversion": self.lineEdit_reversion.text(),
#             "income_cost": self.lineEdit_income_cost.text()
#         }

#         # Сохраняем таблицу доходов
#         income_table = []
#         for row in range(self.tableWidget_income_cost.rowCount()):
#             row_data = []
#             for col in range(self.tableWidget_income_cost.columnCount()):
#                 item = self.tableWidget_income_cost.item(row, col)
#                 row_data.append(item.text() if item else "")
#             income_table.append(row_data)
        
#         data["income_table"] = income_table
#         return data




#     def load_income_data(self, data: dict):
#         self.comboBox_rent_type.blockSignals(True)
#         self.comboBox_rent_type.setCurrentText(data.get("rent_type", "Площадь участка"))
#         self.comboBox_rent_type.blockSignals(False)

#         self.lineEdit_living_area.setText(data.get("living_area", ""))
#         """Загружает данные во вкладку доходного подхода"""
#         self.lineEdit_rent.setText(data.get("rent", ""))
#         self.label_rent.setText(data.get("label_rent", ""))
#         self.lineEdit_temp_rent.setText(data.get("temp_rent", ""))
#         self.label_temp.setText(data.get("label_temp", ""))
#         # self.lineEdit_vacancy.setText(data.get("vacancy", ""))
#         # self.lineEdit_nonpayment.setText(data.get("nonpayment", ""))
#         self.lineEdit_collect.setText(data.get("collect", ""))
#         self.label_collect.setText(data.get("label_collect", ""))
#         self.lineEdit_loading.setText(data.get("loading", ""))
#         self.label_loading.setText(data.get("label_loading", ""))
#         self.lineEdit_management.setText(data.get("management", ""))
#         self.label_management.setText(data.get("label_management", ""))
#         self.lineEdit_tax.setText(data.get("tax", ""))
#         self.label_tax.setText(data.get("label_tax", ""))
#         self.lineEdit_discount_rate.setText(data.get("discount_rate", ""))
#         self.lineEdit_capitalization.setText(data.get("capitalization", ""))
#         # self.lineEdit_cap_rate.setText(data.get("cap_rate", ""))
#         # self.lineEdit_living_area.setText(data.get("living_area", ""))
#         # self.comboBox_rent_type.setCurrentText(data.get("rent_type", "Площадь участка"))
#         self.lineEdit_DDP.setText(data.get("ddp", ""))
#         self.lineEdit_reversion.setText(data.get("reversion", ""))
#         self.lineEdit_income_cost.setText(data.get("income_cost", ""))

#         # Восстановление таблицы
#         table_data = data.get("income_table", [])
#         if table_data:
#             self.tableWidget_income_cost.setRowCount(len(table_data))
#             self.tableWidget_income_cost.setColumnCount(len(table_data[0]) if table_data else 0)
#             self.tableWidget_income_cost.setHorizontalHeaderLabels([
#                 "Год", "Годовая аренда", "Коэфф. дисконтирования", "ЧОД", "ДДП"
#             ])
#             for row_idx, row_data in enumerate(table_data):
#                 for col_idx, value in enumerate(row_data):
#                     item = QTableWidgetItem(value)
#                     item.setFlags(item.flags() & ~Qt.ItemIsEditable)
#                     self.tableWidget_income_cost.setItem(row_idx, col_idx, item)


#     def switch_to_comparative(self):
#         """Переключает на вкладку сравнительный подход"""
#         # Найдём индекс вкладки "Сравнительный подход"
#         index = self.valuation_window.tab_widget.indexOf(self.valuation_window.comparative_tab)
#         if index != -1:
#             # Устанавливаем текущую вкладку
#             self.valuation_window.tab_widget.setCurrentIndex(index)
#         self.valuation_window.save_report()