# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        QMainWindow.setObjectName("QMainWindow")
        QMainWindow.resize(300, 465)
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_file_path = QtWidgets.QLabel(self.centralwidget)
        self.label_file_path.setGeometry(QtCore.QRect(0, 340, 300, 16))
        self.label_file_path.setObjectName("label_file_path")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 80, 182, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_login_edu_tatar = QtWidgets.QLabel(self.layoutWidget)
        self.label_login_edu_tatar.setObjectName("label_login_edu_tatar")
        self.gridLayout.addWidget(self.label_login_edu_tatar, 0, 0, 1, 1)
        self.lineEdit_login_edu_tatar = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_login_edu_tatar.setObjectName("lineEdit_login_edu_tatar")
        self.gridLayout.addWidget(self.lineEdit_login_edu_tatar, 0, 1, 1, 1)
        self.label_password_edu_tatar_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_password_edu_tatar_2.setObjectName("label_password_edu_tatar_2")
        self.gridLayout.addWidget(self.label_password_edu_tatar_2, 1, 0, 1, 1)
        self.linEedit_password_edu_tatar = QtWidgets.QLineEdit(self.layoutWidget)
        self.linEedit_password_edu_tatar.setObjectName("linEedit_password_edu_tatar")
        self.gridLayout.addWidget(self.linEedit_password_edu_tatar, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 370, 191, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_close_application = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_close_application.setObjectName("pushButton_close_application")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_close_application)
        self.pushButton_send = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_send.setObjectName("pushButton_send")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_send)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 150, 271, 102))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_link_to_the_folder_food = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_link_to_the_folder_food.setObjectName("lineEdit_link_to_the_folder_food")
        self.verticalLayout.addWidget(self.lineEdit_link_to_the_folder_food)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_link_to_the_page_food = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_link_to_the_page_food.setObjectName("lineEdit_link_to_the_page_food")
        self.verticalLayout.addWidget(self.lineEdit_link_to_the_page_food)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 260, 286, 71))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_save_data = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_save_data.setObjectName("pushButton_save_data")
        self.verticalLayout_2.addWidget(self.pushButton_save_data)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_delete_file = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_delete_file.setObjectName("pushButton_delete_file")
        self.horizontalLayout.addWidget(self.pushButton_delete_file)
        self.pushBatton_download_file = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushBatton_download_file.setObjectName("pushBatton_download_file")
        self.horizontalLayout.addWidget(self.pushBatton_download_file)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 60, 16))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 164, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_proxy = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_proxy.setObjectName("lineEdit_proxy")
        self.horizontalLayout_2.addWidget(self.lineEdit_proxy)
        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(QMainWindow)
        self.action.setObjectName("action")
        self.actionAbout = QtWidgets.QAction(QMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.action_2 = QtWidgets.QAction(QMainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "edu_tatar_ru_food"))
        self.label_file_path.setText(_translate("QMainWindow", "Путь к файлу"))
        self.label_login_edu_tatar.setText(_translate("QMainWindow", "Логин"))
        self.label_password_edu_tatar_2.setText(_translate("QMainWindow", "Пароль"))
        self.pushButton_close_application.setText(_translate("QMainWindow", "Закрыть"))
        self.pushButton_send.setText(_translate("QMainWindow", "Отправить"))
        self.label.setText(_translate("QMainWindow", "Ссылка на папку food:"))
        self.label_2.setText(_translate("QMainWindow", "Ссылка на страницу food:"))
        self.pushButton_save_data.setText(_translate("QMainWindow", "Сохранить"))
        self.pushButton_delete_file.setText(_translate("QMainWindow", "Удалить файл"))
        self.pushBatton_download_file.setText(_translate("QMainWindow", "Загрузить файл"))
        self.label_4.setText(_translate("QMainWindow", "Прокси"))
        self.label_3.setText(_translate("QMainWindow", "http:"))
        self.menu.setTitle(_translate("QMainWindow", "О программе"))
        self.action.setText(_translate("QMainWindow", "Лицензия"))
        self.actionAbout.setText(_translate("QMainWindow", "About"))
        self.action_2.setText(_translate("QMainWindow", "Прокси"))