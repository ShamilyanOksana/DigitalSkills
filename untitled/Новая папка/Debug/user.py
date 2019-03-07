# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from  PyQt5.QtWidgets import QMessageBox
import Crypt
import Contract
import  Lib
import Network
class Ui_Dialog(object):
    Cipto_engine = Crypt.Crypt()
    Encode_Text = None
    file_name = None
    Estate = Contract.Library()
    Login = None
    Password = None
    Station = None
    File_Send = None
    lib = Lib.Lib()
    net = Network.Network()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(757, 584)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tableWidget)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_11.addWidget(self.pushButton_10)
        self.verticalLayout_27.addLayout(self.verticalLayout_11)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_4.addWidget(self.pushButton_24, 0, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_4.addWidget(self.pushButton_25, 0, 1, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_4.addWidget(self.pushButton_26, 0, 3, 1, 1)
        self.verticalLayout_27.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 5, 2, 1, 1)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem1)
        self.label_27 = QtWidgets.QLabel(self.tab_4)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_26.addWidget(self.label_27)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_26.addWidget(self.lineEdit_12)
        self.gridLayout.addLayout(self.verticalLayout_26, 4, 1, 1, 1)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_23.addWidget(self.label_25)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_23.addWidget(self.lineEdit_11)
        self.gridLayout.addLayout(self.verticalLayout_23, 1, 0, 1, 1)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.radioButton = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_24.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_24.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_24.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_24.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_24.addWidget(self.radioButton_5)
        self.gridLayout.addLayout(self.verticalLayout_24, 2, 0, 1, 2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_11.addWidget(self.label_26)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_8 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_5.addWidget(self.radioButton_8)
        self.radioButton_6 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_6.setEnabled(True)
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setAutoRepeat(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_5.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_5.addWidget(self.radioButton_7)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_25.addWidget(self.stackedWidget)
        self.horizontalLayout_11.addLayout(self.verticalLayout_25)
        self.gridLayout.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_22.addWidget(self.label_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_5.addWidget(self.pushButton_11)
        self.verticalLayout_22.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_22, 0, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.label.setText(self.Estate.user_address)

        #Слоты
        self.pushButton_4.clicked.connect(self.hash_file)
        self.pushButton_5.clicked.connect(self.encript_file)
        self.pushButton_6.clicked.connect(self.decript_file)
        self.pushButton_7.clicked.connect(self.save_encode_file)
        self.pushButton_2.clicked.connect(self.request_admin_rights)
        self.pushButton.clicked.connect(self.request_librarian_rights)
        self.pushButton_11.clicked.connect(self.open_file)
        #self.pushButton_3.clicked.connect(self)
        self.pushButton_10.clicked.connect(self.update_main_table)
        self.pushButton_23.clicked.connect(self.send_file)
        self.pushButton_24.clicked.connect(self.confirm_print)
        self.pushButton_25.clicked.connect(self.refuse_print)
        self.pushButton_26.clicked.connect(self.get_file)


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
        self.pushButton_5.setText(_translate("Dialog", "Зашировать файл"))
        self.pushButton_6.setText(_translate("Dialog", "Расшифровать файл"))
        self.pushButton_7.setText(_translate("Dialog", "Сохранить файл"))
        self.label_10.setText(_translate("Dialog", "Симетричный ключ"))
        self.pushButton_8.setText(_translate("Dialog", "Зашировать симетричный ключ"))
        self.pushButton_9.setText(_translate("Dialog", "Расшифровать симетричный ключ"))
        self.label_11.setText(_translate("Dialog", "Зашифрованный симетричный ключ"))
        self.label_12.setText(_translate("Dialog", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Работа с файлами"))
        self.pushButton_10.setText(_translate("Dialog", "Обновить"))
        self.pushButton_24.setText(_translate("Dialog", "Подтведить"))
        self.pushButton_25.setText(_translate("Dialog", "Отклонить"))
        self.pushButton_26.setText(_translate("Dialog", "Запросить файл"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Файлы"))
        self.pushButton_23.setText(_translate("Dialog", "Отправить"))
        self.label_27.setText(_translate("Dialog", "Срок в днях"))
        self.label_25.setText(_translate("Dialog", "Имя файла"))
        self.radioButton.setText(_translate("Dialog", "Печатные издания"))
        self.radioButton_2.setText(_translate("Dialog", "Издания для слепых и слабовидящих"))
        self.radioButton_3.setText(_translate("Dialog", "Официальные документы"))
        self.radioButton_4.setText(_translate("Dialog", "Неопубликованные документы"))
        self.radioButton_5.setText(_translate("Dialog", "Патентные документы"))
        self.label_26.setText(_translate("Dialog", "Категория"))
        self.radioButton_8.setText(_translate("Dialog", "1"))
        self.radioButton_6.setText(_translate("Dialog", "2"))
        self.radioButton_7.setText(_translate("Dialog", "3"))
        self.label_8.setText(_translate("Dialog", "Выберите файл"))
        self.pushButton_11.setText(_translate("Dialog", "Обзор"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Отправить файл"))

        if self.Station == "Lib":
            self.pushButton_6.setEnabled(False)
            Dialog.setWindowTitle(_translate("Dialog", "Библиотекарь"))
            self.tab.setEnabled(False)
            self.Lable_Lib = ["Id", "Название", "Автор", "Тип", "Категория", "Время хранения Коонтракта", "Хэш","Обращение","Время","Успешно"]
            self.pushButton_26.setEnabled(False)
            self.radioButton_8.setEnabled(True)

        else:
            self.pushButton_24.setEnabled(False)
            self.pushButton_25.setEnabled(False)
            self.Lable_Lib = ["Id", "Название", "Автор", "Тип", "Категория", "Время хранения Коонтракта", "Хэш"]
            self.pushButton_26.setEnabled(True)
            self.radioButton_8.setEnabled(False)
            Dialog.setWindowTitle(_translate("Dialog", "Пользователь"))



    def get_file(self):
        Row = self.tableWidget.currentRow()
        Id = self.tableWidget.item(Row, 0).text()
        file_info = {'id': Id,
                     'user_address':self.Estate.user_address
                     }
        Temp =  self.Estate.get_file(file_info)
        if Temp == True:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Успешно!!!")
            self.msg.exec()
        elif Temp=="Сервер не доступен":
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Сервер не доступен!!!")
            self.msg.exec()
        elif Temp=="Wrong category":
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("У вас нет доступа к данной категорий файлов!!!")
            self.msg.exec()



    def confirm_print(self):
        Row = self.tableWidget.currentRow()
        Categri_id = self.tableWidget.item(Row, 4).text()
        Trure_False = self.tableWidget.item(Row, 9).text()
        if Trure_False == "False":
            if Categri_id == "3":
                Id = self.tableWidget.item(Row, 0).text()
                print(Id)
                self.Estate.confirm_print_3(Id)
                print("Принято")
            elif Categri_id == "2":
                Id = self.tableWidget.item(Row, 0).text()
                print(Id)
                self.Estate.confirm_print_2(Id)
                print("Принято")
            #elif Categri_id == ""
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Можно изменять файлы только с флагом False")
            self.msg.exec()



        print(Categri_id)
    def refuse_print(self):
        Row = self.tableWidget.currentRow()
        Categri_id = self.tableWidget.item(Row, 4).text()
        Trure_False = self.tableWidget.item(Row, 9).text()
        if Trure_False == "False":
            if Categri_id == "3":
                Id = self.tableWidget.item(Row, 0).text()
                print(Id)
                self.Estate.refuse_print_3(Id)
                print("Отказанно")
            else:
                Id = self.tableWidget.item(Row, 0).text()
                print(Id)
                self.Estate.refuse_print_2(Id)
                print("Отказанно_")

        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Можно изменять файлы только с флагом False")
            self.msg.exec()




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

    def send_file(self):
        file_name = self.lineEdit_11.text()
        Id = self.Estate.user_address
        print("Id "+Id)
        Arhiv = ""
        Category = ""
        Days = ""
        if self.Station == "User":
            if self.radioButton.isChecked():
                Arhiv = "Печатные издания"
            elif self.radioButton_2.isChecked():
                Arhiv = "Издания для слепых и слабовидящих"
            elif self.radioButton_3.isChecked():
                Arhiv = "Официальные документы"
            elif self.radioButton_4.isChecked():
                Arhiv = "Неопубликованные документы"
            elif self.radioButton_5.isChecked():
                Arhiv = "Патентные документы"
            else:
                print("Выберите архив")
            if self.radioButton_6.isChecked():
                Category = "2"
            elif self.radioButton_7.isChecked():
                Category = "3"
            else:
                print("Вы не выбрали категорию")
            Days = self.lineEdit_12.text()
            if Category == "3":
                Days = "0"
            elif not Days:
                Days = "0"
            # if Category == "2":
            #    data = self.lib.get_file_data(self.File_Send[0])
            #    data_en = self.Cipto_engine.aes_encode(data,"123")
            #    file_info = {'file_name': file_name,
            #                 'data': data_en,
            #                 'author': Id,
            #                 'type': Arhiv,
            #                 'category': Category,
            #                 'timeout': Days}
            #    self.net.send_message(file_info)
            #    print("Оправленно")

            data = self.lib.get_file_data(self.File_Send[0])
            file_info = {'file_name': file_name,
                         'data': data,
                         'author': Id,
                         'type': Arhiv,
                         'category': Category,
                         'timeout': Days}
            self.net.send_message(file_info)
            print("Оправленно")
        elif self.Station =="Lib":
            if self.radioButton.isChecked():
                Arhiv = "Печатные издания"
            elif self.radioButton_2.isChecked():
                Arhiv = "Издания для слепых и слабовидящих"
            elif self.radioButton_3.isChecked():
                Arhiv = "Официальные документы"
            elif self.radioButton_4.isChecked():
                Arhiv = "Неопубликованные документы"
            elif self.radioButton_5.isChecked():
                Arhiv = "Патентные документы"
            else:
                print("Выберите архив")
            if self.radioButton_6.isChecked():
                Category = "2"
            elif self.radioButton_7.isChecked():
                Category = "3"
            elif self.radioButton_8.isChecked():
                Category = "1"
            else:
                print("Вы не выбрали категорию")
            Days = self.lineEdit_12.text()
            if Category == "3" or Category=="1":
                Days = "0"
            elif not Days:
                Days = "0"
            data = self.lib.get_file_data(self.File_Send[0])
            file_info = {'file_name': file_name,
                         'data': data,
                         'author': Id,
                         'type': Arhiv,
                         'category': Category,
                         'timeout': Days}
            self.net.send_message(file_info)
            print("Оправленно")

    def open_file(self):
        self.File_Send = QtWidgets.QFileDialog.getOpenFileName()
        self.lineEdit_5.setText(self.File_Send[0])

    def update_main_table(self):
        if self.Station == "Lib":
            Matrix = self.Estate.show_all_files()
            Lable_Lib = ["Id", "Название", "Автор", "Тип", "Категория", "Время хранения Коонтракта", "Хэш","Обращение","Время","Успешно"]
            self.table_updater(Matrix, self.tableWidget,Lable_Lib)
            print(Matrix)
        else:
            Matrix = self.Estate.show_all_files()  # Нужен метод для заполнения
            Lable_User = ["Id", "Название", "Автор", "Тип", "Категория", "Время хранения Коонтракта", "Хэш"]
            self.table_updater(Matrix, self.tableWidget,Lable_User)



        #self.Estate

    def table_updater(self,Matrix,tableWidget,HeaderLables):
        tableWidget.clear()
        tableWidget.setColumnCount(5)
        tableWidget.setRowCount(5)
        tableWidget.setHorizontalHeaderLabels(HeaderLables)
        if Matrix ==[]:
            print(Matrix,"Matrix is emty")
        else:
            tableWidget.setColumnCount(len(Matrix[0]))
            tableWidget.setRowCount(len(Matrix))
            tableWidget.setHorizontalHeaderLabels(HeaderLables)
            for i in range(len(Matrix)):
                for j in range(len(Matrix[0])):
                    tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(Matrix[i][j]))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

