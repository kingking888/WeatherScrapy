# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 776)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 60, 871, 331))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(21, 17, 841, 311))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Times_Button = QtWidgets.QPushButton(self.widget)
        self.Times_Button.setMinimumSize(QtCore.QSize(50, 25))
        self.Times_Button.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Times_Button.setFont(font)
        self.Times_Button.setStyleSheet("background-color:none;")
        self.Times_Button.setObjectName("Times_Button")
        self.horizontalLayout.addWidget(self.Times_Button)
        self.Dividing_Quality = QtWidgets.QLabel(self.widget)
        self.Dividing_Quality.setMinimumSize(QtCore.QSize(10, 20))
        self.Dividing_Quality.setMaximumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Dividing_Quality.setFont(font)
        self.Dividing_Quality.setStyleSheet("background-color:none;")
        self.Dividing_Quality.setObjectName("Dividing_Quality")
        self.horizontalLayout.addWidget(self.Dividing_Quality)
        self.Day_Button = QtWidgets.QPushButton(self.widget)
        self.Day_Button.setMinimumSize(QtCore.QSize(40, 25))
        self.Day_Button.setMaximumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Day_Button.setFont(font)
        self.Day_Button.setStyleSheet("background-color:none;")
        self.Day_Button.setObjectName("Day_Button")
        self.horizontalLayout.addWidget(self.Day_Button)
        self.Dividing_Quality1 = QtWidgets.QLabel(self.widget)
        self.Dividing_Quality1.setMinimumSize(QtCore.QSize(10, 20))
        self.Dividing_Quality1.setMaximumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Dividing_Quality1.setFont(font)
        self.Dividing_Quality1.setStyleSheet("background-color:none;")
        self.Dividing_Quality1.setObjectName("Dividing_Quality1")
        self.horizontalLayout.addWidget(self.Dividing_Quality1)
        self.Quality_Button = QtWidgets.QPushButton(self.widget)
        self.Quality_Button.setMinimumSize(QtCore.QSize(55, 25))
        self.Quality_Button.setMaximumSize(QtCore.QSize(55, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Quality_Button.setFont(font)
        self.Quality_Button.setStyleSheet("background-color:none;")
        self.Quality_Button.setObjectName("Quality_Button")
        self.horizontalLayout.addWidget(self.Quality_Button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Type_Box = QtWidgets.QComboBox(self.widget)
        self.Type_Box.setMinimumSize(QtCore.QSize(70, 22))
        self.Type_Box.setMaximumSize(QtCore.QSize(70, 22))
        self.Type_Box.setStyleSheet("QComboBox{\n"
"border-color:#C8C8C8;\n"
"color: rgb(80, 80, 80);\n"
"border-style:solid;\n"
"border-width: 0.5 0.5 0.5 0.5;\n"
"border-radius: 4px;\n"
"padding-left: 5px;\n"
"}\n"
"::drop-down{\n"
"    border: none; \n"
"}\n"
"::down-arrow\n"
"{\n"
"    border-image:url(../icon/drop_down.png);\n"
"}\n"
"\n"
"")
        self.Type_Box.setObjectName("Type_Box")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.horizontalLayout.addWidget(self.Type_Box)
        self.View_Box = QtWidgets.QComboBox(self.widget)
        self.View_Box.setMinimumSize(QtCore.QSize(70, 22))
        self.View_Box.setMaximumSize(QtCore.QSize(70, 22))
        self.View_Box.setStyleSheet("QComboBox{\n"
"border-color:#C8C8C8;\n"
"color: rgb(80, 80, 80);\n"
"border-style:solid;\n"
"border-width: 0.5 0.5 0.5 0.5;\n"
"border-radius: 4px;\n"
"padding-left: 7px;\n"
"}\n"
"::drop-down{\n"
"    border: none; \n"
"}\n"
"::down-arrow\n"
"{\n"
"    border-image:url(../icon/drop_down.png);\n"
"}\n"
"\n"
"")
        self.View_Box.setObjectName("View_Box")
        self.View_Box.addItem("")
        self.View_Box.addItem("")
        self.View_Box.addItem("")
        self.horizontalLayout.addWidget(self.View_Box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 270))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 270))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.Times_Button.setText(_translate("MainWindow", "Times"))
        self.Dividing_Quality.setText(_translate("MainWindow", "|"))
        self.Day_Button.setText(_translate("MainWindow", "Day"))
        self.Dividing_Quality1.setText(_translate("MainWindow", "|"))
        self.Quality_Button.setText(_translate("MainWindow", "Quality"))
        self.Type_Box.setItemText(0, _translate("MainWindow", "AQI"))
        self.Type_Box.setItemText(1, _translate("MainWindow", "SO2"))
        self.Type_Box.setItemText(2, _translate("MainWindow", "NO2"))
        self.Type_Box.setItemText(3, _translate("MainWindow", "CO"))
        self.Type_Box.setItemText(4, _translate("MainWindow", "O3"))
        self.Type_Box.setItemText(5, _translate("MainWindow", "PM2.5"))
        self.Type_Box.setItemText(6, _translate("MainWindow", "PM10"))
        self.View_Box.setItemText(0, _translate("MainWindow", "列 表"))
        self.View_Box.setItemText(1, _translate("MainWindow", "曲 线"))
        self.View_Box.setItemText(2, _translate("MainWindow", "圆 饼"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
