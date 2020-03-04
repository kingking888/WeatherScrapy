# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xm_weather.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# PyQt5 包
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QCursor
import sys

# 其他包
from xpinyin import Pinyin
import re, datetime

import matplotlib

# Make sure that we are using QT5,绘制折线图包
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# 自定义包,调用时必须使用绝对路径
from Weather_Spider.spiders.SearchSQL import SearchSQL


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainMnd):
        MainMnd.setObjectName("MainWindow")
        MainMnd.resize(1120, 810)
        MainMnd.setMinimumSize(QtCore.QSize(1120, 810))
        MainMnd.setMaximumSize(QtCore.QSize(1120, 810))

        MainMnd.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        MainMnd.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.centralwidget = QtWidgets.QStackedWidget(MainMnd)
        self.centralwidget.setMinimumSize(QtCore.QSize(1120, 810))
        self.centralwidget.setMaximumSize(QtCore.QSize(1120, 810))
        self.centralwidget.setObjectName("centralwidget")

        self.Left_widget = QtWidgets.QListWidget(self.centralwidget)
        self.Left_widget.setGeometry(QtCore.QRect(0, 0, 245, 810))
        self.Left_widget.setMinimumSize(QtCore.QSize(245, 810))
        self.Left_widget.setMaximumSize(QtCore.QSize(245, 810))
        self.Left_widget.setStyleSheet("background-color: rgb(97, 101, 247);\n"
                                       "border-top-left-radius:10px;\n"
                                       "border-bottom-left-radius:10px;")
        self.Left_widget.setObjectName("Left_widget")
        self.Title_label = QtWidgets.QLabel(self.Left_widget)
        self.Title_label.setGeometry(QtCore.QRect(75, 23, 151, 31))
        self.Title_label.setText("XM-Weather")
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title_label.setFont(font)
        self.Title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_label.setObjectName("Title_label")

        self.layoutWidget = QtWidgets.QWidget(self.Left_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 117, 247, 172))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Dashboard_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Dashboard_Button.setMinimumSize(QtCore.QSize(245, 30))
        self.Dashboard_Button.setMaximumSize(QtCore.QSize(245, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.Dashboard_Button.setFont(font)
        self.Dashboard_Button.setStyleSheet('''
                                             QPushButton{background-image:url(../icon/dashboard_hover.png);
                                             border-radius:0px}
                                             ::hover{background-image:url(../icon/dashboard_hover.png);}
                                             ''')
        self.Dashboard_Button.setObjectName("Dashboard_Button")
        self.Dashboard_Button.clicked.connect(self.dashboardButton)
        self.verticalLayout.addWidget(self.Dashboard_Button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.Statistics_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Statistics_Button.setMinimumSize(QtCore.QSize(245, 30))
        self.Statistics_Button.setMaximumSize(QtCore.QSize(245, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.Statistics_Button.setFont(font)
        self.Statistics_Button.setStyleSheet('''
                                             QPushButton{background-image:url(../icon/statistics.png);
                                             border-radius:0px}
                                             ::hover{background-image:url(../icon/statistics_hover.png);}
                                             ''')
        self.Statistics_Button.setObjectName("Statistics_Button")
        self.Statistics_Button.clicked.connect(self.statisticsButton)

        self.verticalLayout.addWidget(self.Statistics_Button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.Setting_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Setting_Button.setMinimumSize(QtCore.QSize(245, 30))
        self.Setting_Button.setMaximumSize(QtCore.QSize(245, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.Setting_Button.setFont(font)
        self.Setting_Button.setStyleSheet('''
                                         QPushButton{background-image:url(../icon/setting.png);
                                         border-radius:0px}
                                         ::hover{background-image:url(../icon/setting_hover.png);}
                                         ''')
        self.Setting_Button.setText("")
        self.Setting_Button.setObjectName("Setting_Button")
        self.Setting_Button.clicked.connect(self.settingButton)
        self.verticalLayout.addWidget(self.Setting_Button)
        self.Msg_Label = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Label.setGeometry(QtCore.QRect(31, 453, 180, 330))
        self.Msg_Label.setMinimumSize(QtCore.QSize(180, 330))
        self.Msg_Label.setMaximumSize(QtCore.QSize(185, 330))
        self.Msg_Label.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;")
        self.Msg_Label.setText("")
        self.Msg_Label.setObjectName("Msg_Label")

        self.Msg_Icon = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Icon.setGeometry(QtCore.QRect(53, 477, 60, 60))
        self.Msg_Icon.setMinimumSize(QtCore.QSize(60, 60))
        self.Msg_Icon.setMaximumSize(QtCore.QSize(60, 60))
        self.Msg_Icon.setObjectName("Msg_Icon")

        self.Msg_Type = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Type.setGeometry(QtCore.QRect(120, 480, 50, 20))
        self.Msg_Type.setMinimumSize(QtCore.QSize(50, 20))
        self.Msg_Type.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.Msg_Type.setFont(font)
        self.Msg_Type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Type.setObjectName("Msg_Type")

        self.Msg_Time = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Time.setGeometry(QtCore.QRect(121, 511, 50, 15))
        self.Msg_Time.setMinimumSize(QtCore.QSize(50, 15))
        self.Msg_Time.setMaximumSize(QtCore.QSize(50, 15))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.Msg_Time.setFont(font)
        self.Msg_Time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Time.setObjectName("Msg_Time")
        self.Msg_Date = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Date.setGeometry(QtCore.QRect(121, 527, 80, 15))
        self.Msg_Date.setMinimumSize(QtCore.QSize(80, 15))
        self.Msg_Date.setMaximumSize(QtCore.QSize(80, 15))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.Msg_Date.setFont(font)
        self.Msg_Date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Date.setObjectName("Msg_Date")
        self.Msg_Temper = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Temper.setGeometry(QtCore.QRect(31, 560, 180, 60))
        self.Msg_Temper.setMinimumSize(QtCore.QSize(180, 60))
        self.Msg_Temper.setMaximumSize(QtCore.QSize(185, 60))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Msg_Temper.setFont(font)
        self.Msg_Temper.setStyleSheet("border-radius:10px;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.Msg_Temper.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_Temper.setObjectName("Msg_Temper")
        self.Msg_City = QtWidgets.QLabel(self.Left_widget)
        self.Msg_City.setGeometry(QtCore.QRect(31, 621, 180, 25))
        self.Msg_City.setMinimumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.Msg_City.setFont(font)
        self.Msg_City.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_City.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_City.setObjectName("Msg_City")
        self.Msg_Humidity = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Humidity.setGeometry(QtCore.QRect(57, 669, 30, 15))
        self.Msg_Humidity.setMinimumSize(QtCore.QSize(30, 15))
        self.Msg_Humidity.setMaximumSize(QtCore.QSize(30, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Humidity.setFont(font)
        self.Msg_Humidity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Humidity.setObjectName("Msg_Humidity")
        self.Msg_Scale1 = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Scale1.setGeometry(QtCore.QRect(167, 669, 30, 15))
        self.Msg_Scale1.setMinimumSize(QtCore.QSize(30, 15))
        self.Msg_Scale1.setMaximumSize(QtCore.QSize(30, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Scale1.setFont(font)
        self.Msg_Scale1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Scale1.setObjectName("Msg_Scale1")
        self.Msg_Scale2 = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Scale2.setGeometry(QtCore.QRect(167, 719, 30, 15))
        self.Msg_Scale2.setMinimumSize(QtCore.QSize(30, 15))
        self.Msg_Scale2.setMaximumSize(QtCore.QSize(30, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Scale2.setFont(font)
        self.Msg_Scale2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Scale2.setObjectName("Msg_Scale2")
        self.Msg_Precipitation = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Precipitation.setGeometry(QtCore.QRect(57, 719, 40, 15))
        self.Msg_Precipitation.setMinimumSize(QtCore.QSize(40, 15))
        self.Msg_Precipitation.setMaximumSize(QtCore.QSize(40, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Precipitation.setFont(font)
        self.Msg_Precipitation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Precipitation.setObjectName("Msg_Precipitation")
        self.Msg_Bar1 = QtWidgets.QProgressBar(self.Left_widget)
        self.Msg_Bar1.setGeometry(QtCore.QRect(56, 699, 131, 4))
        self.Msg_Bar1.setMinimumSize(QtCore.QSize(131, 4))
        self.Msg_Bar1.setMaximumSize(QtCore.QSize(4, 3))
        self.Msg_Bar1.setStyleSheet(
            "QProgressBar {border: 2px ;   border-radius: 1.5px; background-color: rgb(216, 216, 216);}"
            "::chunk {background-color: rgb(255, 173, 71);}")

        self.Msg_Bar1.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_Bar1.setFormat("")
        self.Msg_Bar1.setObjectName("Msg_Bar1")
        self.Msg_Bar1_2 = QtWidgets.QProgressBar(self.Left_widget)
        self.Msg_Bar1_2.setGeometry(QtCore.QRect(55, 747, 131, 4))
        self.Msg_Bar1_2.setMinimumSize(QtCore.QSize(131, 4))
        self.Msg_Bar1_2.setMaximumSize(QtCore.QSize(4, 3))
        self.Msg_Bar1_2.setStyleSheet("QProgressBar::chunk {background-color: rgb(255, 173, 71);}\n"
                                      "QProgressBar {border: 2px ;   border-radius: 1.5px; background-color: rgb(216, 216, 216);}")

        self.Msg_Bar1_2.setProperty("value", 60)

        self.Msg_Bar1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_Bar1_2.setFormat("")
        self.Msg_Bar1_2.setObjectName("Msg_Bar1_2")
        self.label_3 = QtWidgets.QLabel(self.Left_widget)
        self.label_3.setGeometry(QtCore.QRect(24, 20, 43, 41))
        self.label_3.setMinimumSize(QtCore.QSize(43, 41))
        self.label_3.setMaximumSize(QtCore.QSize(43, 41))
        self.label_3.setStyleSheet("background-image:url(../icon/logo.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")


        self.Right_widget1 = QtWidgets.QWidget(self.centralwidget)
        self.Right_widget1.setGeometry(QtCore.QRect(245, 0, 875, 810))
        self.Right_widget1.setMinimumSize(QtCore.QSize(860, 810))
        self.Right_widget1.setMaximumSize(QtCore.QSize(875, 810))
        self.Right_widget1.setStyleSheet(
            "background-color: rgb(255, 255, 255);border-top-right-radius:10px;border-bottom-right-radius:10px;")
        self.Right_widget1.setObjectName("Right_widget1")

        self.Left_widget.currentRowChanged.connect(self.centralwidget.setCurrentIndex)

        self.City_label = QtWidgets.QLabel(self.Right_widget1)
        self.City_label.setGeometry(QtCore.QRect(30, 77, 54, 30))
        self.City_label.setMinimumSize(QtCore.QSize(0, 30))
        self.City_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.City_label.setFont(font)
        self.City_label.setObjectName("City_label")

        self.Quality_label = QtWidgets.QLabel(self.Right_widget1)
        self.Quality_label.setGeometry(QtCore.QRect(30, 302, 161, 30))
        self.Quality_label.setMinimumSize(QtCore.QSize(161, 30))
        self.Quality_label.setMaximumSize(QtCore.QSize(161, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Quality_label.setFont(font)
        self.Quality_label.setObjectName("Quality_label")
        self.View_label = QtWidgets.QLabel(self.Right_widget1)
        self.View_label.setGeometry(QtCore.QRect(30, 489, 161, 30))
        self.View_label.setMinimumSize(QtCore.QSize(161, 30))
        self.View_label.setMaximumSize(QtCore.QSize(161, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.View_label.setFont(font)
        self.View_label.setObjectName("View_label")
        self.layoutWidget1 = QtWidgets.QWidget(self.Right_widget1)
        self.layoutWidget1.setGeometry(QtCore.QRect(29, 14, 821, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.Search_Layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.Search_Layout.setContentsMargins(0, 0, 0, 0)
        self.Search_Layout.setSpacing(0)
        self.Search_Layout.setObjectName("Search_Layout")
        self.Search_Label = QtWidgets.QLabel(self.layoutWidget1)
        self.Search_Label.setMinimumSize(QtCore.QSize(30, 30))
        self.Search_Label.setMaximumSize(QtCore.QSize(30, 30))

        pixmap = QtGui.QPixmap("../icon/search.png")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        self.Search_Label.setPixmap(pixmap)  # 在label上显示图片
        self.Search_Label.setScaledContents(True)  # 让图片自适应label大小

        self.Search_Label.setObjectName("Search_Label")
        self.Search_Layout.addWidget(self.Search_Label)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.Search_Layout.addItem(spacerItem2)
        self.Search_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Search_lineEdit.setMinimumSize(QtCore.QSize(250, 23))
        self.Search_lineEdit.setMaximumSize(QtCore.QSize(250, 23))
        self.Search_lineEdit.setStyleSheet("border-radius:10px;"
                                           "border-color: rgb(223, 223, 223);"
                                           "border-width: 1px;"
                                           "border-style: solid;"
                                           "padding-left:7px")
        # 输入框提示字符
        self.Search_lineEdit.setPlaceholderText("搜索城市名...")
        self.Search_lineEdit.setObjectName("Search_lineEdit")

        # 文本框回车事件
        self.Search_lineEdit.returnPressed.connect(bCustom.getValue)

        self.Search_Layout.addWidget(self.Search_lineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Search_Layout.addItem(spacerItem3)
        self.User_Button = QtWidgets.QPushButton(self.layoutWidget1)
        self.User_Button.setMinimumSize(QtCore.QSize(33, 33))
        self.User_Button.setMaximumSize(QtCore.QSize(33, 33))
        self.User_Button.setStyleSheet("border-radius:17px;"
                                       "background-image:url(../icon/user.png);")
        self.User_Button.setObjectName("User_Button")
        self.Search_Layout.addWidget(self.User_Button)
        self.Info_Box = QtWidgets.QComboBox(self.layoutWidget1)
        self.Info_Box.setMinimumSize(QtCore.QSize(110, 22))
        self.Info_Box.setMaximumSize(QtCore.QSize(110, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.Info_Box.setFont(font)
        self.Info_Box.setStyleSheet("QComboBox{border-color:#C8C8C8;color: rgb(80, 80, 80);padding-left: 10px;}"
                                    "::drop-down{border: none;}"
                                    "::down-arrow{border-image:url(../icon/drop_down.png);}")
        self.Info_Box.setObjectName("Info_Box")
        self.Info_Box.addItem("")
        self.Info_Box.addItem("")
        self.Info_Box.addItem("")
        self.Info_Box.addItem("")
        self.Search_Layout.addWidget(self.Info_Box)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.Search_Layout.addItem(spacerItem4)
        self.Dividing_Search = QtWidgets.QLabel(self.layoutWidget1)
        self.Dividing_Search.setMinimumSize(QtCore.QSize(10, 20))
        self.Dividing_Search.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(15)
        self.Dividing_Search.setFont(font)
        self.Dividing_Search.setObjectName("Dividing_Search")
        self.Search_Layout.addWidget(self.Dividing_Search)
        spacerItem5 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.Search_Layout.addItem(spacerItem5)
        self.Min_Button = QtWidgets.QPushButton(self.layoutWidget1)
        self.Min_Button.setMinimumSize(QtCore.QSize(25, 25))
        self.Min_Button.setMaximumSize(QtCore.QSize(25, 25))
        self.Min_Button.setStyleSheet(
            "QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}")
        self.Min_Button.setObjectName("Min_Button")
        self.Search_Layout.addWidget(self.Min_Button)
        # 最小化单击事件
        self.Min_Button.clicked.connect(MainMnd.showMinimized)
        # spacerItem6 间隔控件
        # spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.Search_Layout.addItem(spacerItem6)
        # self.Max_Button = QtWidgets.QPushButton(self.layoutWidget1)
        # self.Max_Button.setMinimumSize(QtCore.QSize(25, 25))
        # self.Max_Button.setMaximumSize(QtCore.QSize(25, 25))
        # self.Max_Button.setStyleSheet(
        #     "QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}")
        # self.Max_Button.setObjectName("Max_Button")
        # self.Search_Layout.addWidget(self.Max_Button)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.Search_Layout.addItem(spacerItem7)
        self.Close_Button = QtWidgets.QPushButton(self.layoutWidget1)
        self.Close_Button.setMinimumSize(QtCore.QSize(25, 25))
        self.Close_Button.setMaximumSize(QtCore.QSize(25, 25))
        self.Close_Button.setStyleSheet(
            "QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}")
        self.Close_Button.setObjectName("Close_Button")
        # 关闭单击事件
        self.Close_Button.clicked.connect(MainMnd.close)
        self.Search_Layout.addWidget(self.Close_Button)
        self.City_Scroll = QtWidgets.QScrollArea(self.Right_widget1)
        self.City_Scroll.setGeometry(QtCore.QRect(40, 118, 791, 170))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.City_Scroll.sizePolicy().hasHeightForWidth())

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 3900, 170))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        '''
        1、需要城市数量
        2、需要城市拼音
        3、需要给按钮排序
        '''
        city_name = SearchSQL().city_name[0]
        city_pinyin = SearchSQL().city_name[1]
        self.City_Button = []
        self.City_Dict = {}
        for i in range(len(city_name)):
            self.City_Button.append(i)
            self.City_Button[i] = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.City_Button[i].setMinimumSize(QtCore.QSize(145, 138))
            self.City_Button[i].setMaximumSize(QtCore.QSize(145, 138))
            self.City_Button[i].setObjectName("City_Button")
            self.City_Button[i].setText(f"{city_name[i]}")
            font = QtGui.QFont()
            font.setFamily("等线")
            font.setPointSize(12)
            self.City_Button[i].setFont(font)

            # 此字典，存放按钮拼音名与其号数
            self.City_Dict[city_pinyin[i]] = i

            # 使用self.sender()时class Ui_MainWindow(QMainWindow):括号内必须是QMainWindow,不能是object
            self.City_Button[i].clicked.connect(
                lambda: bCustom.moveButton(self.sender().text()))

            # 默认选中第一个城市
            if i == 0:
                self.City_Button[i].setStyleSheet("QPushButton{"
                                                  "border-radius:10px;"
                                                  "text-align:bottom;"
                                                  "padding-bottom:2px;"
                                                  f"background-image:url(../city_pictures/{city_pinyin[i]}.png);"
                                                  "color: rgb(97, 101, 247);font:Bold 12.5pt '等线';}")
                self.City_Button[i].move(2, 6)
            else:
                self.City_Button[i].setStyleSheet("QPushButton{"
                                                  "border-radius:10px;"
                                                  "text-align:bottom;"
                                                  "padding-bottom:2px;"
                                                  f"background-image:url(../city_pictures/{city_pinyin[i]}.png);"
                                                  "}"
                                                  "QPushButton:hover{color: rgb(97, 101, 247);font:Bold 12.5pt '等线';}")
                self.City_Button[i].move(2 + 180 * i, 18)

        self.City_Scroll.setSizePolicy(sizePolicy)
        self.City_Scroll.setMinimumSize(QtCore.QSize(791, 170))
        self.City_Scroll.setMaximumSize(QtCore.QSize(791, 170))
        self.City_Scroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.City_Scroll.setLineWidth(1)
        self.City_Scroll.setMidLineWidth(0)
        self.City_Scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.City_Scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.City_Scroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.City_Scroll.setWidgetResizable(False)
        self.City_Scroll.setAlignment(QtCore.Qt.AlignCenter)
        self.City_Scroll.setObjectName("City_Scroll")
        self.City_Scroll.setWidget(self.scrollAreaWidgetContents)

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 950, 121))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.Icon_Button = []
        self.Temperature_Button = []
        self.Date_Button = []
        self.label = []
        types = bCustom.weatherButton()
        for i in range(len(types)):
            self.Icon_Button.append(i)
            self.Temperature_Button.append(i)
            self.Date_Button.append(i)
            self.label.append(i)

            self.Icon_Button[i] = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
            self.Icon_Button[i].setMinimumSize(QtCore.QSize(50, 50))
            self.Icon_Button[i].setMaximumSize(QtCore.QSize(50, 50))
            self.Icon_Button[i].setObjectName("Icon_Button")

            self.Temperature_Button[i] = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
            self.Temperature_Button[i].setMinimumSize(QtCore.QSize(80, 20))
            self.Temperature_Button[i].setMaximumSize(QtCore.QSize(80, 20))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(11)
            self.Temperature_Button[i].setFont(font)
            self.Temperature_Button[i].setStyleSheet("border-radius:7px;"
                                                     "background-color:none;")
            self.Temperature_Button[i].setObjectName("Temperature_Button")

            self.Date_Button[i] = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
            self.Date_Button[i].setMinimumSize(QtCore.QSize(80, 23))
            self.Date_Button[i].setMaximumSize(QtCore.QSize(80, 23))
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(12)
            self.Date_Button[i].setFont(font)
            self.Date_Button[i].setStyleSheet("border-radius:7px;\n"
                                              "background-color:none;\n"
                                              "color: rgb(109, 109, 109);\n"
                                              "")
            self.Date_Button[i].setObjectName("Date_Button")

            self.label[i] = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
            self.label[i].setMinimumSize(QtCore.QSize(90, 110))
            self.label[i].setMaximumSize(QtCore.QSize(90, 110))
            self.label[i].setStyleSheet("QPushButton{border-radius:14px;"
                                        "background-color: rgb(247, 247, 247);"
                                        "border-color: rgb(223, 223, 223);"
                                        "border-width: 1px;"
                                        "border-style: solid;}"
                                        "::hover{background:red;}")
            self.label[i].setObjectName("label")

            self.label[i].raise_()
            self.Icon_Button[i].raise_()
            self.Temperature_Button[i].raise_()
            self.Date_Button[i].raise_()

            self.Icon_Button[i].move(22 + 120 * i, 10)
            self.Temperature_Button[i].move(7 + 120 * i, 64)
            self.Date_Button[i].move(7 + 120 * i, 86)
            self.label[i].move(2 + 120 * i, 5)

        self.Air_Scroll = QtWidgets.QScrollArea(self.Right_widget1)
        self.Air_Scroll.setGeometry(QtCore.QRect(40, 346, 791, 121))
        self.Air_Scroll.setMinimumSize(QtCore.QSize(791, 121))
        self.Air_Scroll.setMaximumSize(QtCore.QSize(791, 121))
        self.Air_Scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Air_Scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Air_Scroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Air_Scroll.setWidgetResizable(False)
        self.Air_Scroll.setObjectName("Air_Scroll")
        self.Air_Scroll.setWidget(self.scrollAreaWidgetContents_2)

        self.Times_Button = QtWidgets.QPushButton(self.Right_widget1)
        self.Times_Button.setGeometry(QtCore.QRect(58, 537, 50, 25))
        self.Times_Button.setMinimumSize(QtCore.QSize(50, 25))
        self.Times_Button.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Times_Button.setFont(font)
        self.Times_Button.setStyleSheet("background-color:none;")
        self.Times_Button.setObjectName("Times_Button")
        self.Times_Button.clicked.connect(
            lambda: m.getTable(table=self.sender().text()))

        self.Dividing_Quality = QtWidgets.QLabel(self.Right_widget1)
        self.Dividing_Quality.setGeometry(QtCore.QRect(114, 539, 10, 20))
        self.Dividing_Quality.setMinimumSize(QtCore.QSize(10, 20))
        self.Dividing_Quality.setMaximumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Dividing_Quality.setFont(font)
        self.Dividing_Quality.setStyleSheet("background-color:none;")
        self.Dividing_Quality.setObjectName("Dividing_Quality")

        self.Day_Button = QtWidgets.QPushButton(self.Right_widget1)
        self.Day_Button.setGeometry(QtCore.QRect(130, 537, 40, 25))
        self.Day_Button.setMinimumSize(QtCore.QSize(40, 25))
        self.Day_Button.setMaximumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Day_Button.setFont(font)
        self.Day_Button.setStyleSheet("background-color:none;")
        self.Day_Button.setObjectName("Day_Button")
        self.Day_Button.clicked.connect(
            lambda: m.getTable(table=self.sender().text()))

        # self.Dividing_Quality1 = QtWidgets.QLabel(self.Right_widget1)
        # self.Dividing_Quality1.setGeometry(QtCore.QRect(176, 539, 10, 20))
        # self.Dividing_Quality1.setMinimumSize(QtCore.QSize(10, 20))
        # self.Dividing_Quality1.setMaximumSize(QtCore.QSize(10, 20))
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.Dividing_Quality1.setFont(font)
        # self.Dividing_Quality1.setStyleSheet("background-color:none;")
        # self.Dividing_Quality1.setObjectName("Dividing_Quality1")
        #
        # self.Quality_Button = QtWidgets.QPushButton(self.Right_widget1)
        # self.Quality_Button.setGeometry(QtCore.QRect(192, 537, 55, 25))
        # self.Quality_Button.setMinimumSize(QtCore.QSize(55, 25))
        # self.Quality_Button.setMaximumSize(QtCore.QSize(55, 25))
        # font = QtGui.QFont()
        # font.setFamily("Verdana")
        # self.Quality_Button.setFont(font)
        # self.Quality_Button.setStyleSheet("background-color:none;")
        # self.Quality_Button.setObjectName("Quality_Button")
        # self.Quality_Button.clicked.connect(
        #     lambda: bCustom.drawView(table=self.sender().text()))

        self.Type_Box = QtWidgets.QComboBox(self.Right_widget1)
        self.Type_Box.setGeometry(QtCore.QRect(662, 538, 70, 22))
        self.Type_Box.setMinimumSize(QtCore.QSize(70, 22))
        self.Type_Box.setMaximumSize(QtCore.QSize(70, 22))
        self.Type_Box.setStyleSheet("QComboBox{"
                                    "border-color:#C8C8C8;"
                                    "color: rgb(80, 80, 80);"
                                    "border-style:solid;"
                                    "border-width: 0.5 0.5 0.5 0.5;"
                                    "border-radius: 4px;"
                                    "padding-left: 5px;}"
                                    "::drop-down{border: none; }"
                                    "::down-arrow{border-image:url(../icon/drop_down.png);}")
        self.Type_Box.setObjectName("Type_Box")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.Type_Box.addItem("")
        self.View_Box = QtWidgets.QComboBox(self.Right_widget1)
        self.View_Box.setGeometry(QtCore.QRect(738, 538, 70, 22))
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

        self.Quality_View1 = QtWidgets.QLabel(self.Right_widget1)
        self.Quality_View1.setGeometry(QtCore.QRect(40, 555, 791, 230))
        self.Quality_View1.setMinimumSize(QtCore.QSize(791, 230))
        self.Quality_View1.setMaximumSize(QtCore.QSize(791, 230))
        self.Quality_View1.setStyleSheet("border-radius:10px;\n"
                                         "background-color: rgb(247, 247, 247);\n"
                                         "border-width: 1px;\n"
                                         "border-style: solid;\n"
                                         "border-color:rgb(200,200,200);\n"
                                         "border-top:none;\n"
                                         "border-top-left-radius:0px;\n"
                                         "border-top-right-radius:0px;")
        self.Quality_View1.setText("")
        self.Quality_View1.setObjectName("Quality_View1")
        self.Quality_View = QtWidgets.QLabel(self.Right_widget1)
        self.Quality_View.setGeometry(QtCore.QRect(40, 530, 791, 27))
        self.Quality_View.setMinimumSize(QtCore.QSize(791, 27))
        self.Quality_View.setMaximumSize(QtCore.QSize(791, 27))
        self.Quality_View.setStyleSheet("border-radius:10px;\n"
                                        "background-color: rgb(247, 247, 247);\n"
                                        "border-width: 1px;\n"
                                        "border-style: solid;\n"
                                        "border-color:rgb(200,200,200);\n"
                                        "border-bottom:none;\n"
                                        "border-bottom-left-radius:0px;\n"
                                        "border-bottom-right-radius:0px;")
        self.Quality_View.setText("")
        self.Quality_View.setObjectName("Quality_View")

        self.gridlayout = QtWidgets.QGridLayout(self.Quality_View1)  # 继承容器groupBox

        # m = MyMplCanvas()  # 实例化一个画布对象
        # m.move(0, 0)
        # self.gridlayout.addWidget(m)
        self.Times_Button.raise_()
        self.Dividing_Quality.raise_()
        self.Day_Button.raise_()
        self.View_Box.raise_()
        self.Type_Box.raise_()

        MainMnd.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMnd)
        QtCore.QMetaObject.connectSlotsByName(MainMnd)
        # MainWindow.setTabOrder(self.Search_lineEdit, self.User_Button)
        # MainWindow.setTabOrder(self.User_Button, self.Statistics_Button)
        # MainWindow.setTabOrder(self.Statistics_Button, self.Setting_Button)
        # MainWindow.setTabOrder(self.Setting_Button, ui.Icon_Button[i])
        # MainWindow.setTabOrder(self.Icon_Button[i], self.Temperature_Button)
        # MainWindow.setTabOrder(self.Temperature_Button, self.Date_Button)
        # MainWindow.setTabOrder(self.Date_Button, self.Close_Button)
        # MainWindow.setTabOrder(self.Close_Button, self.Min_Button)
        # MainWindow.setTabOrder(self.Min_Button, self.Quality_Button)
        # MainWindow.setTabOrder(self.Quality_Button, self.View_Box)
        # MainWindow.setTabOrder(self.View_Box, self.Type_Box)
        # MainWindow.setTabOrder(self.Type_Box, self.Times_Button)
        # MainWindow.setTabOrder(self.Times_Button, self.Day_Button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XM-Weathrer"))
        self.Title_label.setText(_translate("MainWindow", "XM-WEATHER"))
        self.Msg_Humidity.setText(_translate("MainWindow", "湿度："))
        self.Msg_Scale1.setText(_translate("MainWindow", "40%"))
        self.Msg_Scale2.setText(_translate("MainWindow", "60%"))
        self.Msg_Precipitation.setText(_translate("MainWindow", "降水量："))
        self.City_label.setText(_translate("MainWindow", "城市"))
        self.Quality_label.setText(_translate("MainWindow", "城市空气质量预报"))
        self.View_label.setText(_translate("MainWindow", "城市空气质量图"))
        self.Info_Box.setItemText(0, _translate("MainWindow", "User_Name"))
        self.Info_Box.setItemText(1, _translate("MainWindow", "个人信息"))
        self.Info_Box.setItemText(2, _translate("MainWindow", "切换帐号"))
        self.Info_Box.setItemText(3, _translate("MainWindow", "退出"))
        self.Dividing_Search.setText(_translate("MainWindow", "|"))
        self.Min_Button.setText(_translate("MainWindow", "—"))
        self.Close_Button.setText(_translate("MainWindow", "X"))
        # self.Dividing_Quality1.setText(_translate("MainWindow", "|"))
        # self.Quality_Button.setText(_translate("MainWindow", "Quality"))
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
        self.Times_Button.setText(_translate("MainWindow", "Times"))
        self.Dividing_Quality.setText(_translate("MainWindow", "|"))
        self.Day_Button.setText(_translate("MainWindow", "Days"))

    def dashboardButton(self):
        self.Dashboard_Button.setStyleSheet('''QPushButton{
                                               background-image:url(../icon/dashboard_hover.png);
                                               border-radius:0px}
                                             ''')
        self.Statistics_Button.setStyleSheet('''QPushButton{
                                                        background-image:url(../icon/statistics.png);
                                                        border-radius:0px}
                                                ::hover{background-image:url(../icon/statistics_hover.png);}
                                            ''')
        self.Setting_Button.setStyleSheet('''QPushButton{
                                                        background-image:url(../icon/setting.png);
                                                        border-radius:0px}
                                                ::hover{background-image:url(../icon/setting_hover.png);}
                                            ''')

    def statisticsButton(self):
        self.Statistics_Button.setStyleSheet('''QPushButton{
                                                       background-image:url(../icon/statistics_hover.png);
                                                       border-radius:0px}
                                                     ''')
        self.Dashboard_Button.setStyleSheet('''QPushButton{
                                                       background-image:url(../icon/dashboard.png);
                                                       border-radius:0px}
                                                ::hover{background-image:url(../icon/dashboard_hover.png);}
                                                     ''')
        self.Setting_Button.setStyleSheet('''QPushButton{
                                                                background-image:url(../icon/setting.png);
                                                                border-radius:0px}
                                                        ::hover{background-image:url(../icon/setting_hover.png);}
                                                    ''')

        self.Right_widget2 = QtWidgets.QWidget(self.centralwidget)
        self.Right_widget2.setGeometry(QtCore.QRect(245, 0, 875, 810))
        self.Right_widget2.setMinimumSize(QtCore.QSize(860, 810))
        self.Right_widget2.setMaximumSize(QtCore.QSize(875, 810))
        self.Right_widget2.setStyleSheet(
            "background-color: rgb(255, 255, 255);border-top-right-radius:10px;border-bottom-right-radius:10px;")
        self.Right_widget2.setObjectName("Right_widget2")


    def settingButton(self):
        self.Setting_Button.setStyleSheet('''QPushButton{
                                                 background-image:url(../icon/setting_hover.png);
                                                 border-radius:0px}
                                        ''')
        self.Statistics_Button.setStyleSheet('''QPushButton{
                                                   background-image:url(../icon/statistics.png);
                                                   border-radius:0px}
                                                ::hover{background-image:url(../icon/statistics_hover.png);}
                                            ''')
        self.Dashboard_Button.setStyleSheet('''QPushButton{
                                                    background-image:url(../icon/dashboard.png);
                                                    border-radius:0px}
                                             ::hover{background-image:url(../icon/dashboard_hover.png);}
                                            ''')


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=79, height=200, dpi=80):
        # 第一步：创建一个创建Figure
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        FigureCanvas.__init__(self, fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = fig.add_subplot(1, 1, 1)
        # 将图标的上边框和有边框去掉
        self.axes.spines['right'].set_color('none')
        self.axes.spines['top'].set_color('none')
        # 动态
        plt.title("aqi")
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # self.drawView()

    # def init_plot(column="AQI", table="times",cityname="成都市"):
    #     x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
    #     self.axes.plot(x, y)
    def getCityname(self, cityname="成都市"):
        cn = cityname
        self.drawView(cityname=cn)

    def getTable(self, table="times"):
        t = table
        self.drawView(table=t)

    def getColumn(self, column="AQI"):
        c = column
        self.drawView(column=c)

    def drawView(self, column="AQI", table="times", cityname="成都市"):
        # 遇到的问题: 在单击按钮时重新绘制散点图的问题和默认生成散点图的问题
        # column =
        table = table.lower()
        datas = SearchSQL().airDatas(column, table, cityname)
        self.x = []
        self.y = []
        for i in range(len(datas)):
            self.y.append(int(datas[i][0]))
            if table == "times":
                self.x.append(datas[i][1].split(' ')[1])
            else:
                self.x.append(datas[i][1])
        self.axes.cla()
        self.axes.plot(self.x, self.y, 'o')
        self.draw()


# 按钮自定义
class ButtonCustom:
    # 在数据库中查找出城市名
    ''' 每次点击都会调用SearchSQL函数，过后需要优化'''
    city_pinyin = SearchSQL().city_name[1]
    # 记录默认按钮的拼音名字和号数
    button_flag = {"new": city_pinyin[0] + "_0", "old": city_pinyin[0] + "_0"}

    # 按钮弹起
    def moveButton(self, button_name="成都市"):
        pinyin = Pinyin()
        city_name = re.sub('-', '', pinyin.get_pinyin(button_name))
        ui.City_Button[ui.City_Dict[city_name]].move(2 + 180 * ui.City_Dict[city_name], 6)
        ui.City_Button[ui.City_Dict[city_name]].setStyleSheet(
            "border-radius:10px;"
            "text-align:bottom;"
            "padding-bottom:2px;"
            f"background-image:url(../city_pictures/{city_name}.png);"
            "color: rgb(97, 101, 247);font:Bold 12.5pt '等线';")

        # 记录新按下的按钮作为老的按钮，下一次按下其他按钮时，可以对老按钮进行还原
        # 它就像一个开关，按下新按钮时关闭旧按钮
        self.button_flag["old"] = self.button_flag["new"]
        # 当按下同一个按钮时不做按钮还原操作
        if self.button_flag["old"] != city_name + "_" + str(ui.City_Dict[city_name]):
            # 按钮还原函数
            self.Reduction(self.button_flag)
        self.button_flag["old"] = self.button_flag["new"]
        self.button_flag["new"] = city_name + "_" + str(ui.City_Dict[city_name])

        self.weatherButton(button_name)  # 天气温度信息 WeatherButton

        self.airButton()

        # MyMplCanvas().drawView(cityname=button_name)

    # 将弹起的按钮还原
    def Reduction(self, name_num):
        # 存放上一个选中按钮的名字和按钮的号数
        old = name_num["old"].split("_")
        ui.City_Button[int(old[1])].move(2 + 180 * int(old[1]), 18)
        ui.City_Button[int(old[1])].setStyleSheet(
            "QPushButton{border-radius:10px;"
            "text-align:bottom;"
            "padding-bottom:2px;"
            f"background-image:url(../city_pictures/{old[0]}.png);"
            "}"
            "QPushButton:hover{color: rgb(97, 101, 247);font:Bold 12.5pt '等线';}")

    def weatherButton(self, button_name="成都市"):
        # Msg_Label的信息生成
        result_msg = SearchSQL().temperature(button_name)  # 查询选中城市的所有的字段数据
        self.times_msg = []
        self.week = []
        self.high_low = []
        self.temperature = []
        self.shidu = []
        self.fx = []
        self.fl = []
        self.types = []
        self.notice = []
        self.cityname = result_msg[1]

        # for i in range(len(result_msg)):
        self.times_msg.append(result_msg[2])
        self.week.append(result_msg[3])
        self.high_low.append(result_msg[4])
        self.temperature.append(result_msg[5])
        self.shidu.append(result_msg[6])
        self.fx.append(result_msg[7])
        self.fl.append(result_msg[8])
        self.types.append(result_msg[9])
        self.notice.append(result_msg[10])

        '''
            1、主要污染物
            2、aqi指数
            3、日期（需要转换）
        '''
        result_pre = SearchSQL().prediction(button_name)
        self.pullutant = result_pre[3].split(",")  # 主要污染物列表
        self.aqi = result_pre[4].split(",")  # api区间
        self.times_pre = []
        for i in range(len(self.pullutant)):
            temp_times = datetime.datetime.now()  # 将文本型日期转换成日期型数据
            delta = datetime.timedelta(days=i)  # 构造往后几天的天数
            n_days = temp_times + delta  # 生成往后几天的日期
            self.times_pre.append(n_days.strftime('%b %d'))

        return self.pullutant

    # 选中城市的天气预报的生成
    def airButton(self):
        # TodayButton内的图标设置
        ui.Msg_Icon.setStyleSheet("background-color:none;")
        pixmap = QtGui.QPixmap(f"../icon/weather/{self.types[0]}.png")
        ui.Msg_Icon.setPixmap(pixmap)  # 在label上显示图片
        ui.Msg_Icon.setScaledContents(True)  # 让图片自适应label大小

        ui.Msg_Type.setText(self.types[0])
        ui.Msg_Time.setText(self.times_msg[0].split(" ")[1])
        ui.Msg_Date.setText(self.times_msg[0].split(" ")[0])
        ui.Msg_Temper.setText(f"{self.temperature[0]}℃")
        ui.Msg_City.setText(self.cityname)
        ui.Msg_Scale1.setText(self.shidu[0])
        ui.Msg_Bar1.setProperty("value", int(re.sub("%", "", self.shidu[0])))

        # Air_Scroll内的图标设置
        for i in range(len(self.pullutant)):
            ui.Icon_Button[i].setStyleSheet("border-radius:7px;"
                                            "background-color:none;"
                                            f"background-image:url(../icon/airQuality/{self.pullutant[i]}.png);"
                                            )
            ui.Temperature_Button[i].setText(self.aqi[i])
            ui.Date_Button[i].setText(self.times_pre[i])

    # def drawView(self, column="AQI", table="times"):
    #     # 遇到的问题: 在单击按钮时重新绘制散点图的问题和默认生成散点图的问题
    #     # column =
    #     table = table.lower()
    #     datas = SearchSQL().airDatas(column, table, self.cityname)
    #     self.x = []
    #     self.y = []
    #     for i in range(len(datas)):
    #         self.y.append(int(datas[i][0]))
    #         if table == "times":
    #             self.x.append(datas[i][1].split(' ')[1])
    #         else:
    #             self.x.append(datas[i][1])
    #     print(self.x, self.y)
    #
    #     # self.canvas = MyMplCanvas(ui.Quality_View)  # 在Quality_View上绘制画板
    #     # ui.gridlayout.addWidget(self.canvas)
    #
    #     MyMplCanvas.axes.clear()
    #     MyMplCanvas.axes.plot(self.x, self.y, 'o')

    def getValue(self):
        print(ui.Search_lineEdit.text())


class XX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_flag = False

    # def keyPressEvent(self, event):
    #     print("12345")
    # def mousePressEvent(self,event):
    #     if event.button() == Qt.LeftButton:
    #         print("鼠标左键点击！")
    #         # print(event.pos().x(),event.pos().y())
    #     if event.button() == Qt.RightButton:
    #         print("鼠标右键点击！")

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            QMouseEvent.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = XX()
    bCustom = ButtonCustom()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    bCustom.moveButton()  # 打开界面后自动生成图片
    MainWindow.show()

    sys.exit(app.exec_())
