'''
    -*- coding: utf-8 -*- 
    @Time : 2020/2/23 15:52 
    @Author : Bulin Liang 
    @File : LeftTabWidget.py 
    @Software: PyCharm
'''

'''
该文件完成功能：
    
'''
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: jyroy
import sys

from PyQt5.QtCore import QUrl
# from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget, QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtCore import QSize, Qt


class LeftTabWidget(QWidget):
    '''左侧选项栏'''

    def __init__(self):
        super(LeftTabWidget, self).__init__()
        self.setObjectName('LeftTabWidget')

        self.setWindowTitle('LeftTabWidget')
        with open('./QListWidgetQSS.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.list_style = f.read()

        self.main_layout = QHBoxLayout(self, spacing=0)  # 窗口的整体布局
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.left_widget = QListWidget()  # 左侧选项列表
        # self.left_widget = QtWidgets.QWidget()
        self.left_widget.setGeometry(QtCore.QRect(0, 300, 0, 0))
        self.left_widget.setMinimumSize(QtCore.QSize(200, 200))
        self.left_widget.setMaximumSize(QtCore.QSize(200, 200))
        self.left_widget.setStyleSheet('''
                    QListWidget::Item:selected {
    background: red;
    border-left: 5px solid rgb(255,255,255);
}
QListWidget::Item:hover {
    border-left: 5px solid red;
}
        ''')
        self.left_widget.setObjectName("left_widget")
        # self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()

    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)  # list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)  # 去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['Dashboard', 'Statistics', 'Seting']
        url_list = ['job_num_wordcloud.html', 'edu_need.html', 'salary_bar.html', 'edu_salary_bar.html']
        self.button = []
        self.widget = []
        for i in range(len(list_str)):
            self.button.append(i)
            self.widget.append(i)
            self.item = QListWidgetItem(QtGui.QIcon("../icon/user.png"), list_str[i], self.left_widget)  # 左侧选项的添加
            self.item.setSizeHint(QSize(0, 60))
            # self.item.setIconSize(QSize(25, 25))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

            self.widget[i] = QtWidgets.QWidget(self.right_widget)
            self.widget[i].setGeometry(QtCore.QRect(0, 0, 875, 810))
            self.widget[i].setMinimumSize(QtCore.QSize(860, 810))
            self.widget[i].setMaximumSize(QtCore.QSize(875, 810))
            self.widget[i].setStyleSheet(
                "background-color: rgb(255, 255, 255);border-top-right-radius:10px;border-bottom-right-radius:10px;")
            self.widget[i].setObjectName("widget")
            self.button[i] = QtWidgets.QPushButton(self.widget[i])
            self.button[i].setText(str(i))
            # self.browser = QWebView()# 右侧用QWebView来显示html网页
            # self.browser.setUrl(QUrl.fromLocalFile('D://python//code//vision//%s' % url_list[i]))
            self.right_widget.addWidget(self.widget[i])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    app.exec()
