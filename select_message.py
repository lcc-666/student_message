# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_message.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_se_Dialog(object):
    def setupUi(self, se_Dialog):
        se_Dialog.setObjectName("se_Dialog")
        se_Dialog.resize(640, 480)
        self.label = QtWidgets.QLabel(se_Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.id_data = QtWidgets.QLineEdit(se_Dialog)
        self.id_data.setGeometry(QtCore.QRect(180, 40, 251, 31))
        self.id_data.setObjectName("id_data")
        self.select = QtWidgets.QPushButton(se_Dialog)
        self.select.setGeometry(QtCore.QRect(490, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.select.setFont(font)
        self.select.setObjectName("select")
        self.label_2 = QtWidgets.QLabel(se_Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 59, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(se_Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 59, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(se_Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 230, 59, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(se_Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 280, 59, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(se_Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 340, 59, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.name = QtWidgets.QTextEdit(se_Dialog)
        self.name.setGeometry(QtCore.QRect(190, 130, 281, 31))
        self.name.setObjectName("name")
        self.sex = QtWidgets.QTextEdit(se_Dialog)
        self.sex.setGeometry(QtCore.QRect(190, 180, 281, 31))
        self.sex.setObjectName("sex")
        self.adress = QtWidgets.QTextEdit(se_Dialog)
        self.adress.setGeometry(QtCore.QRect(190, 230, 281, 31))
        self.adress.setObjectName("adress")
        self.phone = QtWidgets.QTextEdit(se_Dialog)
        self.phone.setGeometry(QtCore.QRect(190, 280, 281, 31))
        self.phone.setObjectName("phone")
        self.major = QtWidgets.QTextEdit(se_Dialog)
        self.major.setGeometry(QtCore.QRect(190, 330, 281, 31))
        self.major.setObjectName("major")
        self.exit = QtWidgets.QPushButton(se_Dialog)
        self.exit.setGeometry(QtCore.QRect(430, 390, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.clear_data = QtWidgets.QPushButton(se_Dialog)
        self.clear_data.setGeometry(QtCore.QRect(80, 400, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.clear_data.setFont(font)
        self.clear_data.setObjectName("clear_data")

        self.retranslateUi(se_Dialog)
        QtCore.QMetaObject.connectSlotsByName(se_Dialog)

    def retranslateUi(self, se_Dialog):
        _translate = QtCore.QCoreApplication.translate
        se_Dialog.setWindowTitle(_translate("se_Dialog", "Dialog"))
        self.label.setText(_translate("se_Dialog", "请输入学号"))
        self.select.setText(_translate("se_Dialog", "查询"))
        self.label_2.setText(_translate("se_Dialog", "姓名"))
        self.label_3.setText(_translate("se_Dialog", "性别"))
        self.label_4.setText(_translate("se_Dialog", "地址"))
        self.label_5.setText(_translate("se_Dialog", "电话"))
        self.label_6.setText(_translate("se_Dialog", "专业"))
        self.exit.setText(_translate("se_Dialog", "退出"))
        self.clear_data.setText(_translate("se_Dialog", "重置"))