# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_message.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_del_Dialog(object):
    def setupUi(self, del_Dialog):
        del_Dialog.setObjectName("del_Dialog")
        del_Dialog.resize(640, 284)
        self.label = QtWidgets.QLabel(del_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.id = QtWidgets.QLineEdit(del_Dialog)
        self.id.setGeometry(QtCore.QRect(200, 80, 211, 41))
        self.id.setObjectName("id")
        self.delete_message = QtWidgets.QPushButton(del_Dialog)
        self.delete_message.setGeometry(QtCore.QRect(450, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.delete_message.setFont(font)
        self.delete_message.setObjectName("delete_message")
        self.exit = QtWidgets.QPushButton(del_Dialog)
        self.exit.setGeometry(QtCore.QRect(390, 190, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.clear_data = QtWidgets.QPushButton(del_Dialog)
        self.clear_data.setGeometry(QtCore.QRect(90, 190, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.clear_data.setFont(font)
        self.clear_data.setObjectName("clear_data")

        self.retranslateUi(del_Dialog)
        QtCore.QMetaObject.connectSlotsByName(del_Dialog)

    def retranslateUi(self, del_Dialog):
        _translate = QtCore.QCoreApplication.translate
        del_Dialog.setWindowTitle(_translate("del_Dialog", "Dialog"))
        self.label.setText(_translate("del_Dialog", "请输入学号"))
        self.delete_message.setText(_translate("del_Dialog", "删除"))
        self.exit.setText(_translate("del_Dialog", "退出"))
        self.clear_data.setText(_translate("del_Dialog", "重置"))
