# from PyQt5.QtWidgets import QDialog, QPushButton, QCheckBox, QTextBrowser
# from PyQt5 import uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
# import os

# class CollectLossesDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "collect_losses_dialog.ui"), self)
        

#         self.pushButton_collect_losses_ok = self.findChild(QPushButton, "pushButton_collect_losses_ok")
#         self.pushButton_collect_losses_ok.clicked.connect(self.accept)

#         self.checkBox_min = self.findChild(QCheckBox, "checkBox_min")
#         self.checkBox_min.clicked.connect(self.single_selection)
#         self.checkBox_min.setText('Минимальные потери (2%) — объект стабильно сдан, арендаторы надёжны, задержек по оплате не возникает')

#         self.checkBox_mean = self.findChild(QCheckBox, "checkBox_mean")
#         self.checkBox_mean.clicked.connect(self.single_selection)

#         self.checkBox_mean.setText(' Средние потери (3.5%) — периодическая смена арендаторов, возможны краткосрочные простои и просрочки')

#         self.checkBox_max = self.findChild(QCheckBox, "checkBox_max")
#         self.checkBox_max.clicked.connect(self.single_selection)

#         self.checkBox_max.setText('Максимальные потери (5%) — высокая текучесть арендаторов, объект удалён, дисциплина платежей слабая')

#         self.textBrowser_collect_losses = self.findChild(QTextBrowser, "textBrowser_collect_losses")
#         font = QFont("Georgia", 12)
#         self.textBrowser_collect_losses.setFont(font)
#         self.textBrowser_collect_losses.setAlignment(Qt.AlignLeft)
#         self.checkboxes = [self.checkBox_min, self.checkBox_mean, self.checkBox_max]
#         collect_losses_text = (
#             'В мировой практике для жилых домов, сдаваемых в аренду, потери от недосбора аренды\n'
#             '(вакантность и риск неплатежей) составляют в среднем от 2% до 5% от\n'
#             'годовой потенциальной выручки.\n'
#             'Конкретное значение зависит от стабильности арендаторов, удалённости объекта,\n'
#             'спроса на аренду и качества управления.'
#         )

#         self.textBrowser_collect_losses.setText(collect_losses_text)
#         self.textBrowser_collect_losses.setReadOnly(True)

#     def get_selected_collect_losses(self):
#         if self.checkBox_min.isChecked():
#             return "Минимальные потери", 0.02
#         elif self.checkBox_mean.isChecked():
#             return "Средние потери", 0.035
#         elif self.checkBox_max.isChecked():
#             return "Максимальные потери", 0.05
#         return "Не выбрано", 0.0

#     def single_selection(self):
#         """Выбор только одного чекбокса"""
#         sender = self.sender()
#         for cb in self.checkboxes:
#             if cb != sender:
#                 cb.setChecked(False)