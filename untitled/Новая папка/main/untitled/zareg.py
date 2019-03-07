# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zareg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import Contract
import user
class Ui_Dialog(object):
    Estate = user.Ui_Dialog.Estate
    User_Ui = user.Ui_Dialog()
    login = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 337)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(140, 140, 141, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)

        #Слоты
        self.pushButton_2.clicked.connect(self.zareg)
        self.pushButton.clicked.connect(self.auto)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите имя"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.pushButton_2.setText(_translate("Dialog", "Зарегестрироватся"))
    def auto(self):
        State = self.Estate.check_in(self.login)
        if State =="Ваш аккаунт заблокирован":
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ваш аккаунт заблокирован")
            self.msg.exec()
        elif State == "Вы не зарегестрированы":
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Вы не зарегестрированы")
            self.msg.exec()
        elif State =="Admin":
            #self.Admin_Ui.Estate.auth_geth(login, password)
            self.Admin_Window = QtWidgets.QDialog()
            self.Admin_Ui.setupUi(self.Admin_Window)
            self.Admin_Window.show()
        elif State == "Lib":
           # Station = self.Zareg_Ui.User_Ui.Estate.auth_geth(login, password)
            self.User_Ui.Station = State
            #self.User_Ui.Password = password
            #self.User_Ui.Login = login
            self.Window = QtWidgets.QDialog()
            self.User_Ui.setupUi(self.Window)
            self.Window.show()
        elif State =="User":
            #self.Estate.auth_geth(login,password)
            self.User_Window = QtWidgets.QDialog()
            self.User_Ui.setupUi(self.User_Window)
            self.User_Window.show()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Неправельный логин или пароль")
            self.msg.exec()
    def zareg(self):
        name = self.lineEdit.text()
        if name == "":
            name = " "
        self.Estate.new_ok_ck(name)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Файл с закрытым ключем создан в дериктории программы ")
        msg.exec()
        self.User_Window = QtWidgets.QDialog()
        self.User_Ui.setupUi(self.User_Window)
        self.User_Window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

