# from PyQt5.QtWidgets import QDialog, QPushButton, QTextBrowser
# from PyQt5 import uic
# import os

# class TaxDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         uic.loadUi(os.path.join(os.path.dirname(__file__), "tax_dialog.ui"), self)

#         self.textBrowser_tax_table = self.findChild(QTextBrowser, "textBrowser_tax_table")
#         self.pushButton_tax_agree = self.findChild(QPushButton, "pushButton_tax_agree")

#         self.fill_tax_info()
#         self.pushButton_tax_agree.clicked.connect(self.accept)

#     def fill_tax_info(self):
#         html_table = """
#         <table border="1" cellspacing="0" cellpadding="6" width="100%">
#         <tr><th>№</th><th>Объекты налогообложения</th><th>Налоговая ставка (%)</th></tr>
#         <tr><td>1</td><td>Жилые дома и квартиры, дачные строения (до 200 кв.м включительно), машино-место и др.</td><td>0,34</td></tr>
#         <tr><td>2</td><td>Жилые дома и квартиры в городах:</td><td></td></tr>
#         <tr><td></td><td>— свыше 200 кв.м до 500 кв.м</td><td>0,45</td></tr>
#         <tr><td></td><td>— свыше 500 кв.м</td><td>0,6</td></tr>
#         <tr><td>3</td><td>Жилые дома в прочих населённых пунктах свыше 200 кв.м</td><td>0,45</td></tr>
#         <tr><td>4</td><td>Объекты для предпринимательской деятельности или сдачи в аренду</td><td>1,5</td></tr>
#         </table>
#         """
#         self.textBrowser_tax_table.setHtml(html_table)
