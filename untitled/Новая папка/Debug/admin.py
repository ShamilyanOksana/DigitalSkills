# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import Contract
class Ui_Dialog(object):
    Leabl_1 = ["Адрес пользователя","Имя","Категория","Роль","Открытый ключ"]
    Estate = Contract.Library()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 755)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_9.addWidget(self.tableWidget_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_5.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tableWidget_4)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_11.addWidget(self.pushButton_11)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_8.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Слоты
        self.pushButton_3.clicked.connect(self.show_reqest_roles)
        self.pushButton.clicked.connect(self.enable_user)
        self.pushButton_9.clicked.connect(self.showAllUsers)
        self.pushButton_10.clicked.connect(self.delete_user)
        self.pushButton_2.clicked.connect(self.refuse_rights)
        self.pushButton_6.clicked.connect(self.show_request_category)
        self.pushButton_11.clicked.connect(self.update_files)





    def Zapros_Roli(self):
        Matrix = [["lol","123","Test"],["lol","123","Test"],["lol","123","Test"]]
        Lable = ["one","two","three"]
        self.table_updater(Matrix,self.tableWidget,Lable)
    def update_files(self):
        Matrix = self.Estate.show_all_files()  # Нужен метод для заполнения
        Lable_User = ["Id", "Название", "Автор", "Тип", "Категория", "Время хранения Коонтракта", "Хэш"]
        self.table_updater(Matrix, self.tableWidget_4, Lable_User)

    def delete_user(self):
        Row = self.tableWidget_3.currentRow()
        Item = self.tableWidget_3.item(Row, 0).text()
        print(Item)
        self.Estate.delete_user(Item)
    def enable_user(self):
        self.confirm_rights()
    def showAllUsers(self):
        Matrix = self.Estate.show_all_users()
        Lable = ["Адресс пользователя","Имя","Категория","Роль","Открытый ключ"]
        self.table_updater(Matrix,self.tableWidget_3,Lable)
        print(Matrix)
    def show_request_category(self):
        Matrix = self.Estate.show_request_category()
        List = ["Адресс пользователя","Категория"]
        self.table_updater(Matrix,self.tableWidget_2,List)

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
    def confirm_rights(self):
        Row = self.tableWidget.currentRow()
        user_adr = self.tableWidget.item(Row, 0).text()
        role = self.tableWidget.item(Row, 1).text()
        self.Estate.confirm_rights(user_adr,role)
    def refuse_rights(self):
        Row = self.tableWidget.currentRow()
        user_adr = self.tableWidget.item(Row, 0).text()
        role = self.tableWidget.item(Row, 1).text()
        print(user_adr)
        print(role)
        self.Estate.refuse_rights(user_adr, role)

    def show_reqest_roles(self):
        Matrix = self.Estate.show_request_roles()
        Lable = ["Адрес пользователя","Роль"]
        print(Matrix)

        self.table_updater(Matrix,self.tableWidget,Lable)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Запросы роли"))
        self.pushButton.setText(_translate("Dialog", "Принять "))
        self.pushButton_2.setText(_translate("Dialog", "Откозать"))
        self.pushButton_3.setText(_translate("Dialog", "Обновить таблицу"))
        self.label_2.setText(_translate("Dialog", "Запросы категории"))
        self.pushButton_4.setText(_translate("Dialog", "Принять "))
        self.pushButton_5.setText(_translate("Dialog", "Откозать"))
        self.pushButton_6.setText(_translate("Dialog", "Обновить таблицу"))
        self.label_3.setText(_translate("Dialog", "Адресс пользователя"))
        self.pushButton_7.setText(_translate("Dialog", "Удалить"))
        self.label_4.setText(_translate("Dialog", "Адресс библиотекоря"))
        self.pushButton_8.setText(_translate("Dialog", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Запросы"))
        self.pushButton_10.setText(_translate("Dialog", "Удалить пользователя"))
        self.pushButton_9.setText(_translate("Dialog", "Обновить таблицу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Список пользователей"))
        self.pushButton_11.setText(_translate("Dialog", "Обновить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Список файлов"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

