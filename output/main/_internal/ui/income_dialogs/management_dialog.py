# from PyQt5.QtWidgets import QDialog, QPushButton, QCheckBox, QTextBrowser
# from PyQt5 import uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
# import os

# class ManagementDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "management_dialog.ui"), self)
        

#         self.pushButton_management_ok = self.findChild(QPushButton, "pushButton_management_ok")
#         self.pushButton_management_ok.clicked.connect(self.accept)

#         self.checkBox_min = self.findChild(QCheckBox, "checkBox_min")
#         self.checkBox_min.clicked.connect(self.single_selection)
#         self.checkBox_min.setText('Минимальные расходы (3%) — управление собственником, объект находится рядом, минимальное вмешательство')

#         self.checkBox_mean = self.findChild(QCheckBox, "checkBox_mean")
#         self.checkBox_mean.clicked.connect(self.single_selection)

#         self.checkBox_mean.setText('Средние расходы (4.5%) — периодическое участие сторонних специалистов (управляющий, ремонтники)')

#         self.checkBox_max = self.findChild(QCheckBox, "checkBox_max")
#         self.checkBox_max.clicked.connect(self.single_selection)

#         self.checkBox_max.setText('Максимальные расходы (6%) — управление полностью передано сторонней компании, объект удалён, требуется постоянный контроль')

#         self.textBrowser_management = self.findChild(QTextBrowser, "textBrowser_management")
#         font = QFont("Georgia", 12)
#         self.textBrowser_management.setFont(font)
#         self.textBrowser_management.setAlignment(Qt.AlignLeft)
#         self.checkboxes = [self.checkBox_min, self.checkBox_mean, self.checkBox_max]
#         management_text = (
#             'В мировой практике для индивидуальных жилых домов (в т.ч. сдаваемых в аренду)\n'
#             'расходы на управление принимаются в пределах:\n'
#             'от 3% до 6% от годовой валовой арендной выручки, в зависимости от\n'
#             'характера управления и удаленности объекта.'
#         )

#         self.textBrowser_management.setText(management_text)
#         self.textBrowser_management.setReadOnly(True)

#     def get_selected_management_risk(self):
#         if self.checkBox_min.isChecked():
#             return "Минимальные расходы", 0.03
#         elif self.checkBox_mean.isChecked():
#             return "Средние расходы", 0.045
#         elif self.checkBox_max.isChecked():
#             return "Максимальные расходы", 0.06
#         return "Не выбрано", 0.0

#     def single_selection(self):
#         """Выбор только одного чекбокса"""
#         sender = self.sender()
#         for cb in self.checkboxes:
#             if cb != sender:
#                 cb.setChecked(False)