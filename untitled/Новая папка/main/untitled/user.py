# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import QMessageBox
import Crypt
import Contract
class Ui_Dialog(object):
    Cipto_engine = Crypt.Crypt()
    Encode_Text = None
    file_name = None
    Estate = Contract.Library()
    Login = None
    Password = None
    Station = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(692, 570)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_6.addWidget(self.lineEdit_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_6.addWidget(self.pushButton_7)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_7.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_7.addWidget(self.pushButton_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.label.setText(self.Estate.user_address)

        #Слоты
        self.pushButton_4.clicked.connect(self.hash_file)
        self.pushButton_5.clicked.connect(self.encript_file)
        self.pushButton_6.clicked.connect(self.decript_file)
        self.pushButton_7.clicked.connect(self.save_encode_file)
        self.pushButton_2.clicked.connect(self.request_admin_rights)
        self.pushButton.clicked.connect(self.request_librarian_rights)
        #self.pushButton_3.clicked.connect(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Ваш адрес "))
        self.label.setText(_translate("Dialog", "Adr"))
        self.label_4.setText(_translate("Dialog", "Подать запрос на роль библиотекоря"))
        self.pushButton.setText(_translate("Dialog", "Подать"))
        self.label_3.setText(_translate("Dialog", "Подать запрос на роль администратора"))
        self.pushButton_2.setText(_translate("Dialog", "Подать"))
        self.label_5.setText(_translate("Dialog", "Подать запрос на доступ к категории \"Прочая тайна\""))
        self.pushButton_3.setText(_translate("Dialog", "Подать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("Dialog", "Подать запросы для адменистратора"))
        self.label_6.setText(_translate("Dialog", "Название файла"))
        self.pushButton_4.setText(_translate("Dialog", "Выроботать хэш"))
        self.label_7.setText(_translate("Dialog", "Хэш:"))
        self.label_9.setText(_translate("Dialog", "Симетричный ключ"))
        self.pushButton_5.setText(_translate("Dialog", "Зашифровать файл"))
        self.pushButton_6.setText(_translate("Dialog", "Расшифровать файл"))
        self.pushButton_7.setText(_translate("Dialog", "Сохранить файл"))
        self.label_10.setText(_translate("Dialog", "Симетричный ключ"))
        self.pushButton_8.setText(_translate("Dialog", "Зашифровать симетричный ключ"))
        self.pushButton_9.setText(_translate("Dialog", "Расшифровать симетричный ключ"))
        self.label_11.setText(_translate("Dialog", "Зашифрованный симетричный ключ"))
        self.label_12.setText(_translate("Dialog", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Работа с файлами"))
        if self.Station == "Lib":
            self.pushButton_6.setEnabled(False)
            Dialog.setWindowTitle(_translate("Dialog", "Библиотекарь"))
            self.tab.setEnabled(False)


    def hash_file(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName()
        self.lineEdit.setText(self.file[0])
        Hash = self.Cipto_engine.get_hash(self.file[0])
        self.lineEdit_4.setText(Hash)
    def save_encode_file(self):
        self.file_name = QtWidgets.QFileDialog.getSaveFileName()
        with open(self.file_name[0], 'wb') as file_Encode:
            file_Encode.write(self.Encode_Text)
    def encript_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName()
        cimetric_key = self.lineEdit_2.text()
        text = b''
        with open(self.file_name[0],'rb') as file:
            for i in file:
                text += i
        self.Encode_Text = self.Cipto_engine.aes_encode(text,cimetric_key)
    def decript_file(self):
        text = b''
        cimetric_key = self.lineEdit_2.text()
        self.file_name = QtWidgets.QFileDialog.getOpenFileName()
        with open(self.file_name[0],'rb') as file_Decode:
            for i in file_Decode:
                text +=i
        self.Decode_text = self.Cipto_engine.aes_decode(text,cimetric_key)
        with open("Decoded.txt",'wb')as decoded_file:
            decoded_file.write(self.Decode_text)
    def encript_cimetric_key(self):
        Text_key = self.lineEdit_3.text()
        key = "123"
    def request_admin_rights(self):
        self.Estate.request_admin_rights()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Отправленно")
        msg.exec()
    def request_librarian_rights(self):
        self.Estate.request_librarian_rights()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Отправленно")
        msg.exec()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

