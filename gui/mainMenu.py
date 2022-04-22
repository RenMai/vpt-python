# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(924, 606)
        self.central_widget = QtWidgets.QWidget(mainWindow)
        self.central_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.central_widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.central_widget)
        self.tabWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.mainWin = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWin.sizePolicy().hasHeightForWidth())
        self.mainWin.setSizePolicy(sizePolicy)
        self.mainWin.setObjectName("mainWin")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainWin)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startBtn = QtWidgets.QPushButton(self.mainWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setMinimumSize(QtCore.QSize(0, 70))
        self.startBtn.setBaseSize(QtCore.QSize(0, 0))
        self.startBtn.setAcceptDrops(False)
        self.startBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startBtn.setAutoFillBackground(False)
        self.startBtn.setObjectName("startBtn")
        self.buttonGroup = QtWidgets.QButtonGroup(mainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.startBtn)
        self.verticalLayout_2.addWidget(self.startBtn)
        self.saveBtn = QtWidgets.QPushButton(self.mainWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy)
        self.saveBtn.setMinimumSize(QtCore.QSize(0, 70))
        self.saveBtn.setObjectName("saveBtn")
        self.buttonGroup.addButton(self.saveBtn)
        self.verticalLayout_2.addWidget(self.saveBtn)
        self.addBtn = QtWidgets.QPushButton(self.mainWin)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout_2.addWidget(self.addBtn)
        self.delBtn = QtWidgets.QPushButton(self.mainWin)
        self.delBtn.setObjectName("delBtn")
        self.verticalLayout_2.addWidget(self.delBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.mainWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.tableWidget = QtWidgets.QTableWidget(self.mainWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.mainWin, "")
        self.autoTab = QtWidgets.QWidget()
        self.autoTab.setObjectName("autoTab")
        self.autoKsBtn = QtWidgets.QPushButton(self.autoTab)
        self.autoKsBtn.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.autoKsBtn.setObjectName("autoKsBtn")
        self.pushButton_2 = QtWidgets.QPushButton(self.autoTab)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.autoTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        mainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "VPT All In One"))
        self.startBtn.setText(_translate("mainWindow", "Start"))
        self.saveBtn.setText(_translate("mainWindow", "Save"))
        self.addBtn.setText(_translate("mainWindow", "Thêm Acc"))
        self.delBtn.setText(_translate("mainWindow", "Xoá Acc"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "link"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "group"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainWin), _translate("mainWindow", "Main Window"))
        self.autoKsBtn.setText(_translate("mainWindow", "auto Ks"))
        self.pushButton_2.setText(_translate("mainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.autoTab), _translate("mainWindow", "auto"))