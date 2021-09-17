# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        #   background
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap(":/newprefix2/metal.jpg")))
        self.setPalette(palette)
        Dialog.setObjectName("Dialog")
        Dialog.resize(189, 133)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 30, 95, 65))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.move_1 = QtWidgets.QPushButton(self.widget)
        self.move_1.setObjectName("move_1")
        self.verticalLayout.addWidget(self.move_1)
        self.move_2 = QtWidgets.QPushButton(self.widget)
        self.move_2.setObjectName("move_2")
        self.verticalLayout.addWidget(self.move_2)
        ico = QtGui.QIcon()
        ico.addPixmap(QtGui.QPixmap("ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(ico)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.move_1.setText(_translate("Dialog", "移动一根"))
        self.move_2.setText(_translate("Dialog", "移动两根"))
