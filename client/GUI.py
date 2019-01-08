# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import json
import requests
# import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from aip import AipImageCensor
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(862, 490)
        Form.setStyleSheet("#Form{background-image: url(./imgs/bg.jpg);\n"
"background-repeat:repeat-xy;}\n")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 10, 211, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: blue;")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(370, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(720, 160, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 120, 51, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(460, 120, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(700, 20, 101, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 240, 141, 131))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_3.setGeometry(QtCore.QRect(180, 240, 141, 131))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_4.setGeometry(QtCore.QRect(350, 240, 141, 131))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_5.setGeometry(QtCore.QRect(520, 240, 141, 131))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.graphicsView_6 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_6.setGeometry(QtCore.QRect(690, 240, 141, 131))
        self.graphicsView_6.setObjectName("graphicsView_6")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.open_img)
        self.pushButton.clicked.connect(self.get_data)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "行人重识别"))
        self.label.setText(_translate("Form", "行人重识别展示"))
        self.label_3.setText(_translate("Form", "Match"))
        self.pushButton.setText(_translate("Form", "query"))
        self.pushButton_2.setText(_translate("Form", "open"))

    def open_img(self):
        file_path, _ = QFileDialog.getOpenFileName(self.Form, "选择图片",
    r"./query/0342")
        img = QImage()
        img.load(file_path)  # 载入图片
        self.img = img
        self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
        self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)
        self.lineEdit.setText(file_path)
        # with open(file_path, 'rb') as f:
        #     image = f.read()
        # self.img = image

    def show_img(self,addrs,index):
        if index == 1:
            img = QImage()
            img.load(addrs)  # 载入图片
            self.img = img
            self.img = img.scaled(self.graphicsView_2.width(), self.graphicsView_2.height())
            self.graphicsView_2.scene = QGraphicsScene()  # 创建一个图片元素的对象
            self.graphicsView_2.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
            self.graphicsView_2.setScene(self.graphicsView_2.scene)
        elif index == 2:
            img = QImage()
            img.load(addrs)  # 载入图片
            self.img = img
            self.img = img.scaled(self.graphicsView_3.width(), self.graphicsView_3.height())
            self.graphicsView_3.scene = QGraphicsScene()  # 创建一个图片元素的对象
            self.graphicsView_3.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
            self.graphicsView_3.setScene(self.graphicsView_3.scene)
        elif index == 3:
            img = QImage()
            img.load(addrs)  # 载入图片
            self.img = img
            self.img = img.scaled(self.graphicsView_4.width(), self.graphicsView_4.height())
            self.graphicsView_4.scene = QGraphicsScene()  # 创建一个图片元素的对象
            self.graphicsView_4.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
            self.graphicsView_4.setScene(self.graphicsView_4.scene)
        elif index == 4:
            img = QImage()
            img.load(addrs)  # 载入图片
            self.img = img
            self.img = img.scaled(self.graphicsView_5.width(), self.graphicsView_5.height())
            self.graphicsView_5.scene = QGraphicsScene()  # 创建一个图片元素的对象
            self.graphicsView_5.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
            self.graphicsView_5.setScene(self.graphicsView_5.scene)

        elif index == 5:
            img = QImage()
            img.load(addrs)  # 载入图片
            self.img = img
            self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
            self.graphicsView_6.scene = QGraphicsScene()  # 创建一个图片元素的对象
            self.graphicsView_6.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
            self.graphicsView_6.setScene(self.graphicsView_6.scene)

        
    def get_data(self):
        try:
            base_url = 'http://172.16.22.125:8000/api/data/Perter?q='
            index = '777'
            url = base_url+index
            data = requests.get(url, timeout=5).text
            if data:
                data = json.loads(data)
                print("---data---", data)
                img_addrs = data['detail']
                i=1
                for img in img_addrs:
                    addrs = r'./gallary'
                    addrs += img[11:]
                    print('----addrs---', addrs)
                    self.show_img(addrs, i)
                    i += 1
                    if i == 6:
                        break
        except Exception as e:
            message = str(e)+'：后台服务器在局域网中，无法连接'
            QMessageBox.critical(self.Form, "没有连接到后台服务器", message)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
