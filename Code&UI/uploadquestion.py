# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadquestion.ui'
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
        Dialog.resize(381, 283)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(101, 81, 173, 143))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.upload_submit = QtWidgets.QPushButton(self.layoutWidget)
        self.upload_submit.setObjectName("upload_submit")
        self.verticalLayout.addWidget(self.upload_submit)
        self.back = QtWidgets.QPushButton(self.layoutWidget)
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)
        ico = QtGui.QIcon()
        ico.addPixmap(QtGui.QPixmap("ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(ico)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "出题"))
        self.label.setText(_translate("Dialog", "请在下方输入您的等式"))
        self.upload_submit.setText(_translate("Dialog", "提交"))
        self.back.setText(_translate("Dialog", "返回"))
