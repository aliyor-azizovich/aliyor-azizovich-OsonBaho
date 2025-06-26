# from PyQt5.QtWidgets import QDialog, QTextEdit, QPushButton
# from PyQt5 import uic
# from PyQt5.QtGui import QTextCursor, QFont
# from PyQt5.QtCore import Qt
# import os

# class CapitalizationDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "capitalization_dialog.ui"), self)

#         # Привязка элементов UI
#         self.textEdit_capitalization_description = self.findChild(QTextEdit, "textEdit_capitalization_description")
#         self.pushButton_agree = self.findChild(QPushButton, "pushButton_agree")

#         # Устанавливаем красивый шрифт и выравнивание по центру
#         font = QFont("Georgia", 12)  # Пример: шрифт Georgia, размер 12
#         self.textEdit_capitalization_description.setFont(font)
#         self.textEdit_capitalization_description.setAlignment(Qt.AlignLeft)  # QTextEdit не поддерживает AlignCenter напрямую

#         # Устанавливаем текст обоснования
#         justification_text = (
#             "В соответствии с положениями Единого национального стандарта оценки имущества (ЕНСО),\n"
#             "терминальная ставка капитализации может быть определена как разница между ставкой дисконтирования\n"
#             "и надбавкой за индивидуальный риск объекта.\n\n"
#             "Такой подход отражает рыночные ожидания доходности типового стабилизированного актива,\n"
#             "исключая специфические риски, присущие конкретному оцениваемому объекту.\n\n"
#             "В данном случае ставка капитализации определена как:\n"
#             "Ставка дисконтирования минус индивидуальный риск."
#         )
#         self.textEdit_capitalization_description.setText(justification_text)
#         self.textEdit_capitalization_description.setReadOnly(True)

#         # Центрирование курсора на начало текста
#         cursor = self.textEdit_capitalization_description.textCursor()
#         cursor.movePosition(QTextCursor.Start)
#         self.textEdit_capitalization_description.setTextCursor(cursor)

#         # Кнопка закрытия
#         self.pushButton_agree.clicked.connect(self.accept)
   
   
   