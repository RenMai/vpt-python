# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tacticalmove.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 210)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 10, 158, 152))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.verticalLayout.addWidget(self.lineEdit1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.verticalLayout.addWidget(self.lineEdit2)
        self.lineEdit3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit3.setObjectName("lineEdit3")
        self.verticalLayout.addWidget(self.lineEdit3)
        self.lineEdit4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit4.setObjectName("lineEdit4")
        self.verticalLayout.addWidget(self.lineEdit4)
        self.lineEdit5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit5.setObjectName("lineEdit5")
        self.verticalLayout.addWidget(self.lineEdit5)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(250, 120, 75, 23))
        self.startBtn.setObjectName("startBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 71, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 344, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "auto"))
        self.label.setText(_translate("MainWindow", "window title"))
        self.startBtn.setText(_translate("MainWindow", "start"))
        self.label_2.setText(_translate("MainWindow", "Top Left"))
        self.label_3.setText(_translate("MainWindow", "Top Right"))
        self.label_4.setText(_translate("MainWindow", "Bottom Left"))
        self.label_5.setText(_translate("MainWindow", "Middle"))
        self.label_6.setText(_translate("MainWindow", "Bottom Right"))
