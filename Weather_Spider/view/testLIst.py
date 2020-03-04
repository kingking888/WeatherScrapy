# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testLIst.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QCursor

import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 810)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 810))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 810))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Left_widget = QtWidgets.QWidget(self.centralwidget)
        self.Left_widget.setGeometry(QtCore.QRect(0, 0, 245, 810))
        self.Left_widget.setMinimumSize(QtCore.QSize(245, 810))
        self.Left_widget.setMaximumSize(QtCore.QSize(245, 810))
        self.Left_widget.setStyleSheet("background-color: rgb(97, 101, 247);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.Left_widget.setObjectName("Left_widget")
        self.List_widget = QtWidgets.QListWidget(self.Left_widget)
        self.List_widget.setGeometry(QtCore.QRect(0, 129, 245, 171))
        self.List_widget.setMinimumSize(QtCore.QSize(245, 0))
        self.List_widget.setMaximumSize(QtCore.QSize(245, 245))
        self.List_widget.setStyleSheet("QListWidget::Item:selected {\n"
"    border-left: 5px solid rgb(255,255,255);\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QListWidget::Item:hover {\n"
"    border-left: 5px solid rgb(255,255,255);\n"
"}")
        self.List_widget.setLineWidth(1)
        self.List_widget.setIconSize(QtCore.QSize(60, 60))
        self.List_widget.setModelColumn(0)
        self.List_widget.setObjectName("List_widget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.List_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.List_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.List_widget.addItem(item)
        self.Title_label = QtWidgets.QLabel(self.Left_widget)
        self.Title_label.setGeometry(QtCore.QRect(71, 28, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title_label.setFont(font)
        self.Title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_label.setObjectName("Title_label")
        self.label_3 = QtWidgets.QLabel(self.Left_widget)
        self.label_3.setGeometry(QtCore.QRect(20, 25, 43, 41))
        self.label_3.setMinimumSize(QtCore.QSize(43, 41))
        self.label_3.setMaximumSize(QtCore.QSize(43, 41))
        self.label_3.setStyleSheet("background-image:url(../icon/logo.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Msg_Precipitation = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Precipitation.setGeometry(QtCore.QRect(59, 717, 40, 15))
        self.Msg_Precipitation.setMinimumSize(QtCore.QSize(40, 15))
        self.Msg_Precipitation.setMaximumSize(QtCore.QSize(40, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Precipitation.setFont(font)
        self.Msg_Precipitation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Precipitation.setObjectName("Msg_Precipitation")
        self.Msg_Date = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Date.setGeometry(QtCore.QRect(123, 525, 80, 15))
        self.Msg_Date.setMinimumSize(QtCore.QSize(80, 15))
        self.Msg_Date.setMaximumSize(QtCore.QSize(80, 15))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.Msg_Date.setFont(font)
        self.Msg_Date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Date.setObjectName("Msg_Date")
        self.Msg_Temper = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Temper.setGeometry(QtCore.QRect(33, 558, 180, 60))
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
        self.Msg_Time = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Time.setGeometry(QtCore.QRect(123, 509, 50, 15))
        self.Msg_Time.setMinimumSize(QtCore.QSize(50, 15))
        self.Msg_Time.setMaximumSize(QtCore.QSize(50, 15))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.Msg_Time.setFont(font)
        self.Msg_Time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Time.setObjectName("Msg_Time")
        self.Msg_Label = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Label.setGeometry(QtCore.QRect(33, 451, 180, 330))
        self.Msg_Label.setMinimumSize(QtCore.QSize(180, 330))
        self.Msg_Label.setMaximumSize(QtCore.QSize(185, 330))
        self.Msg_Label.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;")
        self.Msg_Label.setText("")
        self.Msg_Label.setObjectName("Msg_Label")
        self.Msg_Scale1 = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Scale1.setGeometry(QtCore.QRect(169, 667, 30, 15))
        self.Msg_Scale1.setMinimumSize(QtCore.QSize(30, 15))
        self.Msg_Scale1.setMaximumSize(QtCore.QSize(30, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Scale1.setFont(font)
        self.Msg_Scale1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Scale1.setObjectName("Msg_Scale1")
        self.Msg_City = QtWidgets.QLabel(self.Left_widget)
        self.Msg_City.setGeometry(QtCore.QRect(33, 619, 180, 25))
        self.Msg_City.setMinimumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.Msg_City.setFont(font)
        self.Msg_City.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_City.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_City.setObjectName("Msg_City")
        self.Msg_Bar1_2 = QtWidgets.QProgressBar(self.Left_widget)
        self.Msg_Bar1_2.setGeometry(QtCore.QRect(57, 745, 131, 4))
        self.Msg_Bar1_2.setMinimumSize(QtCore.QSize(131, 4))
        self.Msg_Bar1_2.setMaximumSize(QtCore.QSize(4, 3))
        self.Msg_Bar1_2.setStyleSheet("QProgressBar::chunk {background-color: rgb(255, 173, 71);}\n"
"QProgressBar {border: 2px ;   border-radius: 1.5px; background-color: rgb(216, 216, 216);}\n"
"\n"
"")
        self.Msg_Bar1_2.setProperty("value", 60)
        self.Msg_Bar1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_Bar1_2.setFormat("")
        self.Msg_Bar1_2.setObjectName("Msg_Bar1_2")
        self.Msg_Scale2 = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Scale2.setGeometry(QtCore.QRect(169, 717, 30, 15))
        self.Msg_Scale2.setMinimumSize(QtCore.QSize(30, 15))
        self.Msg_Scale2.setMaximumSize(QtCore.QSize(30, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Scale2.setFont(font)
        self.Msg_Scale2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Scale2.setObjectName("Msg_Scale2")
        self.Msg_Days = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Days.setGeometry(QtCore.QRect(122, 478, 50, 20))
        self.Msg_Days.setMinimumSize(QtCore.QSize(50, 20))
        self.Msg_Days.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.Msg_Days.setFont(font)
        self.Msg_Days.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Days.setObjectName("Msg_Days")
        self.Msg_Bar1 = QtWidgets.QProgressBar(self.Left_widget)
        self.Msg_Bar1.setGeometry(QtCore.QRect(58, 697, 131, 4))
        self.Msg_Bar1.setMinimumSize(QtCore.QSize(131, 4))
        self.Msg_Bar1.setMaximumSize(QtCore.QSize(4, 3))
        self.Msg_Bar1.setStyleSheet("QProgressBar {border: 2px ;   border-radius: 1.5px; background-color: rgb(216, 216, 216);}\n"
"::chunk {background-color: rgb(255, 173, 71);}\n"
"\n"
"")
        self.Msg_Bar1.setProperty("value", 60)
        self.Msg_Bar1.setAlignment(QtCore.Qt.AlignCenter)
        self.Msg_Bar1.setFormat("")
        self.Msg_Bar1.setObjectName("Msg_Bar1")
        self.Msg_icon = QtWidgets.QLabel(self.Left_widget)
        self.Msg_icon.setGeometry(QtCore.QRect(55, 477, 60, 60))
        self.Msg_icon.setMinimumSize(QtCore.QSize(60, 60))
        self.Msg_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.Msg_icon.setStyleSheet("border-radius:10px;\n"
"background-image:url(../icon/quality.png);\n"
"background-color:none;")
        self.Msg_icon.setText("")
        self.Msg_icon.setObjectName("Msg_icon")
        self.Msg_Humidity = QtWidgets.QLabel(self.Left_widget)
        self.Msg_Humidity.setGeometry(QtCore.QRect(59, 667, 30, 15))
        self.Msg_Humidity.setMinimumSize(QtCore.QSize(30, 15))
        self.Msg_Humidity.setMaximumSize(QtCore.QSize(30, 15))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.Msg_Humidity.setFont(font)
        self.Msg_Humidity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Msg_Humidity.setObjectName("Msg_Humidity")
        self.List_widget.raise_()
        self.Title_label.raise_()
        self.label_3.raise_()
        self.Msg_Label.raise_()
        self.Msg_Scale1.raise_()
        self.Msg_City.raise_()
        self.Msg_Bar1_2.raise_()
        self.Msg_Scale2.raise_()
        self.Msg_Days.raise_()
        self.Msg_Bar1.raise_()
        self.Msg_icon.raise_()
        self.Msg_Humidity.raise_()
        self.Msg_Precipitation.raise_()
        self.Msg_Time.raise_()
        self.Msg_Temper.raise_()
        self.Msg_Date.raise_()
        self.Right_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.Right_widget.setGeometry(QtCore.QRect(245, 310, 875, 500))
        self.Right_widget.setMinimumSize(QtCore.QSize(875, 500))
        self.Right_widget.setMaximumSize(QtCore.QSize(875, 500))
        self.Right_widget.setStyleSheet("border-bottom-right-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.Right_widget.setObjectName("Right_widget")
        self.Page1 = QtWidgets.QWidget()
        self.Page1.setStyleSheet("")
        self.Page1.setObjectName("Page1")
        self.Air_Scroll = QtWidgets.QScrollArea(self.Page1)
        self.Air_Scroll.setGeometry(QtCore.QRect(44, 50, 791, 121))
        self.Air_Scroll.setMinimumSize(QtCore.QSize(791, 121))
        self.Air_Scroll.setMaximumSize(QtCore.QSize(791, 121))
        self.Air_Scroll.setWidgetResizable(True)
        self.Air_Scroll.setObjectName("Air_Scroll")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 791, 121))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.Icon_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Icon_Button.setGeometry(QtCore.QRect(22, 10, 50, 50))
        self.Icon_Button.setMinimumSize(QtCore.QSize(50, 50))
        self.Icon_Button.setMaximumSize(QtCore.QSize(50, 50))
        self.Icon_Button.setStyleSheet("border-radius:0px;\n"
"background-color:none;\n"
"background-image:url(../icon/airQuality/pm10.png);")
        self.Icon_Button.setText("")
        self.Icon_Button.setObjectName("Icon_Button")
        self.Temperature_Back = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Temperature_Back.setGeometry(QtCore.QRect(2, 5, 90, 110))
        self.Temperature_Back.setMinimumSize(QtCore.QSize(90, 110))
        self.Temperature_Back.setMaximumSize(QtCore.QSize(90, 110))
        self.Temperature_Back.setStyleSheet("border-radius:14px;\n"
"background-color: rgb(247, 247, 247);\n"
"border-color: rgb(223, 223, 223);\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.Temperature_Back.setText("")
        self.Temperature_Back.setObjectName("Temperature_Back")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label.setGeometry(QtCore.QRect(7, 64, 80, 20))
        self.label.setMinimumSize(QtCore.QSize(80, 20))
        self.label.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius:0px;\n"
"background-color:none;")
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setGeometry(QtCore.QRect(7, 88, 80, 20))
        self.label_2.setMinimumSize(QtCore.QSize(80, 20))
        self.label_2.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius:0px;\n"
"background-color:none;")
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Temperature_Back_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Temperature_Back_2.setGeometry(QtCore.QRect(140, 8, 90, 110))
        self.Temperature_Back_2.setMinimumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_2.setMaximumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_2.setStyleSheet("border-radius:14px;\n"
"background-color: rgb(247, 247, 247);\n"
"border-color: rgb(223, 223, 223);\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.Temperature_Back_2.setText("")
        self.Temperature_Back_2.setObjectName("Temperature_Back_2")
        self.Temperature_Back_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Temperature_Back_3.setGeometry(QtCore.QRect(262, 8, 90, 110))
        self.Temperature_Back_3.setMinimumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_3.setMaximumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_3.setStyleSheet("border-radius:14px;\n"
"background-color: rgb(247, 247, 247);\n"
"border-color: rgb(223, 223, 223);\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.Temperature_Back_3.setText("")
        self.Temperature_Back_3.setObjectName("Temperature_Back_3")
        self.Temperature_Back_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Temperature_Back_4.setGeometry(QtCore.QRect(380, 10, 90, 110))
        self.Temperature_Back_4.setMinimumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_4.setMaximumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_4.setStyleSheet("border-radius:14px;\n"
"background-color: rgb(247, 247, 247);\n"
"border-color: rgb(223, 223, 223);\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.Temperature_Back_4.setText("")
        self.Temperature_Back_4.setObjectName("Temperature_Back_4")
        self.Temperature_Back_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Temperature_Back_5.setGeometry(QtCore.QRect(510, 10, 90, 110))
        self.Temperature_Back_5.setMinimumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_5.setMaximumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_5.setStyleSheet("border-radius:14px;\n"
"background-color: rgb(247, 247, 247);\n"
"border-color: rgb(223, 223, 223);\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.Temperature_Back_5.setText("")
        self.Temperature_Back_5.setObjectName("Temperature_Back_5")
        self.Temperature_Back_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Temperature_Back_6.setGeometry(QtCore.QRect(630, 10, 90, 110))
        self.Temperature_Back_6.setMinimumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_6.setMaximumSize(QtCore.QSize(90, 110))
        self.Temperature_Back_6.setStyleSheet("border-radius:14px;\n"
"background-color: rgb(247, 247, 247);\n"
"border-color: rgb(223, 223, 223);\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.Temperature_Back_6.setText("")
        self.Temperature_Back_6.setObjectName("Temperature_Back_6")
        self.Temperature_Back.raise_()
        self.Icon_Button.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.Temperature_Back_2.raise_()
        self.Temperature_Back_3.raise_()
        self.Temperature_Back_4.raise_()
        self.Temperature_Back_5.raise_()
        self.Temperature_Back_6.raise_()
        self.Air_Scroll.setWidget(self.scrollAreaWidgetContents_3)
        self.Quality_label = QtWidgets.QLabel(self.Page1)
        self.Quality_label.setGeometry(QtCore.QRect(34, -2, 161, 30))
        self.Quality_label.setMinimumSize(QtCore.QSize(0, 30))
        self.Quality_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Quality_label.setFont(font)
        self.Quality_label.setObjectName("Quality_label")
        self.Right_widget.addWidget(self.Page1)
        self.Page2 = QtWidgets.QWidget()
        self.Page2.setStyleSheet("")
        self.Page2.setObjectName("Page2")
        self.Dividing_Quality = QtWidgets.QLabel(self.Page2)
        self.Dividing_Quality.setGeometry(QtCore.QRect(116, 51, 10, 20))
        self.Dividing_Quality.setMinimumSize(QtCore.QSize(10, 20))
        self.Dividing_Quality.setMaximumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Dividing_Quality.setFont(font)
        self.Dividing_Quality.setStyleSheet("background-color:none;")
        self.Dividing_Quality.setObjectName("Dividing_Quality")
        self.Day_Button = QtWidgets.QPushButton(self.Page2)
        self.Day_Button.setGeometry(QtCore.QRect(132, 49, 40, 25))
        self.Day_Button.setMinimumSize(QtCore.QSize(40, 25))
        self.Day_Button.setMaximumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Day_Button.setFont(font)
        self.Day_Button.setStyleSheet("background-color:none;")
        self.Day_Button.setObjectName("Day_Button")
        self.View_Box = QtWidgets.QComboBox(self.Page2)
        self.View_Box.setGeometry(QtCore.QRect(740, 50, 70, 22))
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
        self.Times_Button = QtWidgets.QPushButton(self.Page2)
        self.Times_Button.setGeometry(QtCore.QRect(60, 49, 50, 25))
        self.Times_Button.setMinimumSize(QtCore.QSize(50, 25))
        self.Times_Button.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Times_Button.setFont(font)
        self.Times_Button.setStyleSheet("background-color:none;")
        self.Times_Button.setObjectName("Times_Button")
        self.Dividing_Quality1 = QtWidgets.QLabel(self.Page2)
        self.Dividing_Quality1.setGeometry(QtCore.QRect(178, 51, 10, 20))
        self.Dividing_Quality1.setMinimumSize(QtCore.QSize(10, 20))
        self.Dividing_Quality1.setMaximumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Dividing_Quality1.setFont(font)
        self.Dividing_Quality1.setStyleSheet("background-color:none;")
        self.Dividing_Quality1.setObjectName("Dividing_Quality1")
        self.View_label = QtWidgets.QLabel(self.Page2)
        self.View_label.setGeometry(QtCore.QRect(34, -2, 191, 30))
        self.View_label.setMinimumSize(QtCore.QSize(0, 30))
        self.View_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.View_label.setFont(font)
        self.View_label.setObjectName("View_label")
        self.Quality_Button = QtWidgets.QPushButton(self.Page2)
        self.Quality_Button.setGeometry(QtCore.QRect(194, 49, 55, 25))
        self.Quality_Button.setMinimumSize(QtCore.QSize(55, 25))
        self.Quality_Button.setMaximumSize(QtCore.QSize(55, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Quality_Button.setFont(font)
        self.Quality_Button.setStyleSheet("background-color:none;")
        self.Quality_Button.setObjectName("Quality_Button")
        self.Type_Box = QtWidgets.QComboBox(self.Page2)
        self.Type_Box.setGeometry(QtCore.QRect(664, 50, 70, 22))
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
        self.Right_widget.addWidget(self.Page2)
        self.Page3 = QtWidgets.QWidget()
        self.Page3.setObjectName("Page3")
        self.Right_widget.addWidget(self.Page3)
        self.Search_group = QtWidgets.QGroupBox(self.centralwidget)
        self.Search_group.setGeometry(QtCore.QRect(245, 0, 875, 311))
        self.Search_group.setMinimumSize(QtCore.QSize(875, 311))
        self.Search_group.setMaximumSize(QtCore.QSize(875, 311))
        self.Search_group.setStyleSheet("border-top-right-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.Search_group.setTitle("")
        self.Search_group.setObjectName("Search_group")
        self.User_Button_2 = QtWidgets.QPushButton(self.Search_group)
        self.User_Button_2.setGeometry(QtCore.QRect(609, 18, 33, 33))
        self.User_Button_2.setMinimumSize(QtCore.QSize(33, 33))
        self.User_Button_2.setMaximumSize(QtCore.QSize(33, 33))
        self.User_Button_2.setStyleSheet("border-radius:17px;\n"
"background-image:url(../icon/user.png);\n"
"\n"
"")
        self.User_Button_2.setText("")
        self.User_Button_2.setObjectName("User_Button_2")
        self.Dividing_Search_2 = QtWidgets.QLabel(self.Search_group)
        self.Dividing_Search_2.setGeometry(QtCore.QRect(769, 25, 8, 20))
        self.Dividing_Search_2.setMinimumSize(QtCore.QSize(8, 20))
        self.Dividing_Search_2.setMaximumSize(QtCore.QSize(8, 20))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(15)
        self.Dividing_Search_2.setFont(font)
        self.Dividing_Search_2.setObjectName("Dividing_Search_2")
        self.Close_Button_2 = QtWidgets.QPushButton(self.Search_group)
        self.Close_Button_2.setGeometry(QtCore.QRect(828, 22, 25, 25))
        self.Close_Button_2.setMinimumSize(QtCore.QSize(25, 25))
        self.Close_Button_2.setMaximumSize(QtCore.QSize(25, 25))
        self.Close_Button_2.setStyleSheet("QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}")
        self.Close_Button_2.setObjectName("Close_Button_2")
        self.Info_Box_2 = QtWidgets.QComboBox(self.Search_group)
        self.Info_Box_2.setGeometry(QtCore.QRect(646, 24, 110, 22))
        self.Info_Box_2.setMinimumSize(QtCore.QSize(110, 22))
        self.Info_Box_2.setMaximumSize(QtCore.QSize(110, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.Info_Box_2.setFont(font)
        self.Info_Box_2.setStyleSheet("QComboBox{\n"
"border-color:#C8C8C8;\n"
"color: rgb(80, 80, 80);\n"
"padding-left: 10px;\n"
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
        self.Info_Box_2.setObjectName("Info_Box_2")
        self.Info_Box_2.addItem("")
        self.Info_Box_2.addItem("")
        self.Info_Box_2.addItem("")
        self.Info_Box_2.addItem("")
        self.Min_Button_2 = QtWidgets.QPushButton(self.Search_group)
        self.Min_Button_2.setGeometry(QtCore.QRect(793, 22, 25, 25))
        self.Min_Button_2.setMinimumSize(QtCore.QSize(25, 25))
        self.Min_Button_2.setMaximumSize(QtCore.QSize(25, 25))
        self.Min_Button_2.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:5px;}\n"
"::hover{background:green;}")
        self.Min_Button_2.setObjectName("Min_Button_2")
        self.Search_lineEdit_2 = QtWidgets.QLineEdit(self.Search_group)
        self.Search_lineEdit_2.setGeometry(QtCore.QRect(83, 23, 270, 23))
        self.Search_lineEdit_2.setMinimumSize(QtCore.QSize(270, 23))
        self.Search_lineEdit_2.setMaximumSize(QtCore.QSize(270, 23))
        self.Search_lineEdit_2.setStyleSheet("border-radius:10px;\n"
"border-color: rgb(223, 223, 223);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"padding-left:7px\n"
"")
        self.Search_lineEdit_2.setText("")
        self.Search_lineEdit_2.setObjectName("Search_lineEdit_2")
        self.Search_Label_2 = QtWidgets.QLabel(self.Search_group)
        self.Search_Label_2.setGeometry(QtCore.QRect(22, 15, 40, 40))
        self.Search_Label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.Search_Label_2.setMaximumSize(QtCore.QSize(40, 39))
        self.Search_Label_2.setStyleSheet("background-image:url(./icon/search.png);")
        self.Search_Label_2.setText("")
        self.Search_Label_2.setObjectName("Search_Label_2")
        self.City_Scroll_2 = QtWidgets.QScrollArea(self.Search_group)
        self.City_Scroll_2.setGeometry(QtCore.QRect(41, 124, 791, 170))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.City_Scroll_2.sizePolicy().hasHeightForWidth())
        self.City_Scroll_2.setSizePolicy(sizePolicy)
        self.City_Scroll_2.setMinimumSize(QtCore.QSize(791, 170))
        self.City_Scroll_2.setMaximumSize(QtCore.QSize(791, 170))
        self.City_Scroll_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.City_Scroll_2.setLineWidth(1)
        self.City_Scroll_2.setMidLineWidth(0)
        self.City_Scroll_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.City_Scroll_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.City_Scroll_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.City_Scroll_2.setWidgetResizable(True)
        self.City_Scroll_2.setAlignment(QtCore.Qt.AlignCenter)
        self.City_Scroll_2.setObjectName("City_Scroll_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 791, 170))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.City_Button_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.City_Button_3.setGeometry(QtCore.QRect(2, 18, 145, 110))
        self.City_Button_3.setMinimumSize(QtCore.QSize(145, 110))
        self.City_Button_3.setMaximumSize(QtCore.QSize(145, 110))
        self.City_Button_3.setStyleSheet("background-image:url(../city_pictures/test.png);\n"
"border-radius:10px;")
        self.City_Button_3.setText("")
        self.City_Button_3.setObjectName("City_Button_3")
        self.City_Name_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.City_Name_3.setGeometry(QtCore.QRect(2, 134, 145, 20))
        self.City_Name_3.setMinimumSize(QtCore.QSize(145, 20))
        self.City_Name_3.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.City_Name_3.setFont(font)
        self.City_Name_3.setObjectName("City_Name_3")
        self.City_Scroll_2.setWidget(self.scrollAreaWidgetContents_4)
        self.City_label_2 = QtWidgets.QLabel(self.Search_group)
        self.City_label_2.setGeometry(QtCore.QRect(34, 84, 54, 30))
        self.City_label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.City_label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.City_label_2.setFont(font)
        self.City_label_2.setObjectName("City_label_2")
        self.Search_group.raise_()
        self.Left_widget.raise_()
        self.Right_widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Right_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.List_widget.isSortingEnabled()
        self.List_widget.setSortingEnabled(False)
        item = self.List_widget.item(0)
        item.setText(_translate("MainWindow", "  Dashboard"))
        item = self.List_widget.item(1)
        item.setText(_translate("MainWindow", "Statistics"))
        item = self.List_widget.item(2)
        item.setText(_translate("MainWindow", "Setting   "))
        self.List_widget.setSortingEnabled(__sortingEnabled)
        self.Title_label.setText(_translate("MainWindow", "XM-WEATHER"))
        self.Msg_Precipitation.setText(_translate("MainWindow", "降水量："))
        self.Msg_Date.setText(_translate("MainWindow", "2020/1/28"))
        self.Msg_Temper.setText(_translate("MainWindow", "+26℃"))
        self.Msg_Time.setText(_translate("MainWindow", "20:20"))
        self.Msg_Scale1.setText(_translate("MainWindow", "60%"))
        self.Msg_City.setText(_translate("MainWindow", "德阳"))
        self.Msg_Scale2.setText(_translate("MainWindow", "60%"))
        self.Msg_Days.setText(_translate("MainWindow", "今天"))
        self.Msg_Humidity.setText(_translate("MainWindow", "湿度："))
        self.label.setText(_translate("MainWindow", "100~100"))
        self.label_2.setText(_translate("MainWindow", "11-22"))
        self.Quality_label.setText(_translate("MainWindow", "城市空气质量预报"))
        self.Dividing_Quality.setText(_translate("MainWindow", "|"))
        self.Day_Button.setText(_translate("MainWindow", "Day"))
        self.View_Box.setItemText(0, _translate("MainWindow", "列 表"))
        self.View_Box.setItemText(1, _translate("MainWindow", "曲 线"))
        self.View_Box.setItemText(2, _translate("MainWindow", "圆 饼"))
        self.Times_Button.setText(_translate("MainWindow", "Times"))
        self.Dividing_Quality1.setText(_translate("MainWindow", "|"))
        self.View_label.setText(_translate("MainWindow", "城市空气质量图"))
        self.Quality_Button.setText(_translate("MainWindow", "Quality"))
        self.Type_Box.setItemText(0, _translate("MainWindow", "AQI"))
        self.Type_Box.setItemText(1, _translate("MainWindow", "SO2"))
        self.Type_Box.setItemText(2, _translate("MainWindow", "NO2"))
        self.Type_Box.setItemText(3, _translate("MainWindow", "CO"))
        self.Type_Box.setItemText(4, _translate("MainWindow", "O3"))
        self.Type_Box.setItemText(5, _translate("MainWindow", "PM2.5"))
        self.Type_Box.setItemText(6, _translate("MainWindow", "PM10"))
        self.Dividing_Search_2.setText(_translate("MainWindow", "|"))
        self.Close_Button_2.setText(_translate("MainWindow", "X"))
        self.Info_Box_2.setItemText(0, _translate("MainWindow", "User_Name"))
        self.Info_Box_2.setItemText(1, _translate("MainWindow", "个人信息"))
        self.Info_Box_2.setItemText(2, _translate("MainWindow", "切换帐号"))
        self.Info_Box_2.setItemText(3, _translate("MainWindow", "退出"))
        self.Min_Button_2.setText(_translate("MainWindow", "—"))
        self.City_Name_3.setText(_translate("MainWindow", "成都"))
        self.City_label_2.setText(_translate("MainWindow", "城市"))


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
    # bCustom = ButtonCustom()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # bCustom.moveButton()  # 打开界面后自动生成图片
    MainWindow.show()

    sys.exit(app.exec_())