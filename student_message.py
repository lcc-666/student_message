from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
import sys
from init import *
from insert import *
#插入信息界面
class insert_message(QDialog,Ui_insert_Dialog):
    def __init__(self):
        super(insert_message, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)
        self.ok.clicked.connect(self.insert_sql)

    def insert_sql(self):
        id=int(self.id.text())
        name=self.name.text()
        sex=self.sex.text()
        adress=self.adress.text()
        phone=self.phone.text()
        major=self.major.text()
        tu=(id,name,sex,adress,phone,major)





#初始化界面
class main_dialog(QDialog,Ui_main_Dialog):
    def __init__(self):
        super(main_dialog, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)
        self.insert_xinxi.clicked.connect(self.insert)

    def insert(self):
        dialog=insert_message()
        dialog.exec()







if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Widget=main_dialog()
    Widget.show()
    sys.exit(app.exec_())