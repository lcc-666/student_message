from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
import sys
from sql import *
from init import *
from insert_message import *
from success import *
from updata_message import *
from select_message import *
from delete_message import *

#删除信息
class delete_message(QDialog,Ui_del_Dialog):
    def __init__(self):
        super(delete_message, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)
        self.delete_message.clicked.connect(self.viewdata)
        self.clear_data.clicked.connect(self.clear)

    def viewdata(self):
        id=self.id.text()
        print(id)
        if delete(id)==1:
            dialog=success()
            dialog.exec()
            self.clear()

    def clear(self):
        self.id.clear()

#更新信息
class updata_message(QDialog,Ui_updata_Dialog):
    def __init__(self):
        super(updata_message, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)
        self.clear_data.clicked.connect(self.clear)
        self.ok.clicked.connect(self.updata_sql)

    #导入数据
    def updata_sql(self):
        id=self.id.text()
        name=self.name.text()
        sex=self.sex.text()
        adress=self.adress.text()
        phone=self.phone.text()
        major=self.major.text()
        tu=(id,name,sex,adress,phone,major)
        if updata(tu)==1:
            dialog=success()
            dialog.exec()
            self.clear()

    def clear(self):
        self.id.clear()
        self.name.clear()
        self.sex.clear()
        self.adress.clear()
        self.phone.clear()
        self.major.clear()





#查询信息
class select_message(QDialog,Ui_se_Dialog):
    def __init__(self):
        super(select_message, self).__init__()
        self.setupUi(self)
        self.clear_data.clicked.connect(self.clear)
        self.exit.clicked.connect(self.close)
        self.select.clicked.connect(self.viewdata)

    def viewdata(self):
        id=self.id_data.text()
        xinxi=selects(id)
        self.name.setText(xinxi[0])
        self.sex.setText(xinxi[1])
        self.adress.setText(xinxi[2])
        self.phone.setText(xinxi[3])
        self.major.setText(xinxi[4])

    def clear(self):
        self.name.clear()
        self.sex.clear()
        self.adress.clear()
        self.phone.clear()
        self.major.clear()

#操作成功
class success(QDialog,Ui_su_Dialog):
    def __init__(self):
        super(success, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)



#插入信息界面
class insert_message(QDialog,Ui_insert_Dialog):
    def __init__(self):
        super(insert_message, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)
        self.ok.clicked.connect(self.insert_sql)
        self.clear_data.clicked.connect(self.clear)
    #导入数据
    def insert_sql(self):
        id=self.id.text()
        name=self.name.text()
        sex=self.sex.text()
        adress=self.adress.text()
        phone=self.phone.text()
        major=self.major.text()
        tu=(id,name,sex,adress,phone,major)
        if insert(tu)==1:
            dialog=success()
            dialog.exec()
            self.clear()
    #清空数据
    def clear(self):
        self.id.clear()
        self.name.clear()
        self.sex.clear()
        self.adress.clear()
        self.phone.clear()
        self.major.clear()#


#初始化界面
class main_dialog(QDialog,Ui_main_Dialog):
    def __init__(self):
        super(main_dialog, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)
        self.insert_xinxi.clicked.connect(self.insert)
        self.select_data.clicked.connect(self.select)
        self.update_data.clicked.connect(self.updata)
        self.delete_2.clicked.connect(self.delete)


    def insert(self):
        dialog=insert_message()
        dialog.exec()

    def select(self):
        dialog=select_message()
        dialog.exec()

    def updata(self):
        dialog=updata_message()
        dialog.exec()

    def delete(self):
        dialog=delete_message()
        dialog.exec()


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Widget=main_dialog()
    Widget.show()
    sys.exit(app.exec_())
