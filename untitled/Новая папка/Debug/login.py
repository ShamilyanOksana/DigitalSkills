# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import Contract
import zareg
from PyQt5.QtWidgets import QMessageBox
import admin
import user

class Ui_Dialog(object):
    Estate = Contract.Library()
    Zareg_Ui = zareg.Ui_Dialog()
    Admin_Ui = admin.Ui_Dialog()
    User_Ui = user.Ui_Dialog()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 329)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_8.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        #Слоты
        self.pushButton_2.clicked.connect(self.authorization)
        self.pushButton_3.clicked.connect(self.regestration)
        self.pushButton.clicked.connect(quit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Если у вас есть акаунт"))
        self.label.setText(_translate("Dialog", "Логин:"))
        self.label_2.setText(_translate("Dialog", "Пароль:"))
        self.pushButton.setText(_translate("Dialog", "Выход"))
        self.pushButton_2.setText(_translate("Dialog", "Войти"))
        self.label_4.setText(_translate("Dialog", "Если у вас нет акаунта"))
        self.label_6.setText(_translate("Dialog", "Регестрация"))
        self.label_5.setText(_translate("Dialog", "Пароль:"))
        self.pushButton_3.setText(_translate("Dialog", "Зарегестрироваться"))

    def authorization(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.Zareg_Ui.login = login
        #Test
        Proverka = self.Estate.auth_geth(login, password)
        if Proverka == True:
            if login == "0x280c28e82f000827c8a259ba2a57bd66e89fc54c" and password == "123":
                self.Admin_Ui.Estate.auth_geth(login, password)
                self.Admin_Window = QtWidgets.QDialog()
                self.Admin_Ui.setupUi(self.Admin_Window)
                self.Admin_Window.show()
            # elif login == "0x32a1e697d8d1f0297550634d3be2e477ac0f2695" and password == "123":
            #     self.Admin_Ui.Estate.auth_geth(login, password)
            #     self.Admin_Window = QtWidgets.QDialog()
            #     self.Admin_Ui.setupUi(self.Admin_Window)
            #     self.Admin_Window.show()
            elif login == "0x26ca8e2344cec1ac3ac5765e6f2d74aa688bdf4a" and password == "123":
                Station = self.Zareg_Ui.User_Ui.Estate.auth_geth(login, password)
                self.User_Ui.Station = "Lib"
                self.User_Ui.Password = password
                self.User_Ui.Login = login
                self.Window = QtWidgets.QDialog()
                self.User_Ui.setupUi(self.Window)
                self.Window.show()
            # elif login == "0xe500226ad7c109273cb681ec9ba2c9a18d330409" and password == "123":
            #     Station = self.Zareg_Ui.User_Ui.Estate.auth_geth(login, password)
            #     self.User_Ui.Station = "Lib"
            #     self.User_Ui.Password = password
            #     self.User_Ui.Login = login
            #     self.Window = QtWidgets.QDialog()
            #     self.User_Ui.setupUi(self.Window)
            #     self.Window.show()
            elif login == "0x443D6370ad19A2b695792BAF9A18345001d4e8A7" and password == "123":
                self.User_Ui.Estate.auth_geth("0x443D6370ad19A2b695792BAF9A18345001d4e8A7", "123")
                self.User_Ui.Station = "User"
                self.User_Window = QtWidgets.QDialog()
                self.User_Ui.setupUi(self.User_Window)
                self.User_Window.show()
            else:
                self.Estate.new_ok_ck()
                State = self.Estate.check_in(login)
                if State == "Ваш аккаунт заблокирован":
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Critical)
                    self.msg.setText("Ваш аккаунт заблокирован")
                    self.msg.exec()
                elif State == "Вы не зарегестрированы":
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Critical)
                    self.msg.setText("Вы не зарегестрированы")
                    self.msg.exec()
                elif State == "Admin":
                    self.Admin_Ui.Estate.auth_geth(login, password)
                    self.Admin_Window = QtWidgets.QDialog()
                    self.Admin_Ui.setupUi(self.Admin_Window)
                    self.Admin_Window.show()
                elif State == "Lib":
                    Station = self.Zareg_Ui.User_Ui.Estate.auth_geth(login, password)
                    self.User_Ui.Station = State
                    self.User_Ui.Password = password
                    self.User_Ui.Login = login
                    self.Window = QtWidgets.QDialog()
                    self.User_Ui.setupUi(self.Window)
                    self.Window.show()
                elif State == "User":
                    self.Estate.auth_geth(login, password)
                    self.User_Window = QtWidgets.QDialog()
                    self.User_Ui.setupUi(self.User_Window)
                    self.User_Window.show()
                else:
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Critical)
                    self.msg.setText("Неправельный логин или пароль")
                    self.msg.exec()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Неправельный логин или пароль")
            self.msg.exec()


        # Station = self.Zareg_Ui.Estate.auth_geth(login,password)
        # if login == "0x280c28e82f000827c8a259ba2a57bd66e89fc54c" and password == "123":
        #     self.Admin_Ui.Estate.auth_geth(login,password)
        #     self.Admin_Window = QtWidgets.QDialog()
        #     self.Admin_Ui.setupUi(self.Admin_Window)
        #     self.Admin_Window.show()
        #
        # else:
        #     Station = self.Zareg_Ui.User_Ui.Estate.auth_geth(login, password)
        #     self.Zareg_Ui.User_Ui.Password = password
        #     self.Zareg_Ui.User_Ui.Login = login
        #
        #
        #     if Station == True:
        #         self.Window = QtWidgets.QDialog()
        #         self.Zareg_Ui.setupUi(self.Window)
        #         self.Window.show()
        #     else:
        #         self.msg = QMessageBox()
        #         self.msg.setIcon(QMessageBox.Critical)
        #         self.msg.setText("Неправельный логин или пароль")
        #         self.msg.exec()
        #         print(Station)



    def regestration(self):
        Pasword = self.lineEdit_3.text()
        #Station = self.Zareg_Ui.Estate.new_geth_account(Pasword)
        Station = self.Zareg_Ui.User_Ui.Estate.new_geth_account(Pasword)

        print(Station)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Ваш адрес (логин) "+Station)
        msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



#0x26Ca8e2344cEc1aC3ac5765e6f2D74AA688BDf4A

#0xd6121c9B3d7d0f91B1b4742c349A7B1F60e6e435
