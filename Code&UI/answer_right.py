# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer_right.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_answerright_dialog(object):
    def setupUi(self, answerright_dialog):
        #   background
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap(":/newprefix2/metal.jpg")))
        self.setPalette(palette)
        answerright_dialog.setObjectName("answerright_dialog")
        answerright_dialog.resize(312, 153)
        self.widget = QtWidgets.QWidget(answerright_dialog)
        self.widget.setGeometry(QtCore.QRect(100, 40, 111, 81))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(answerright_dialog)
        QtCore.QMetaObject.connectSlotsByName(answerright_dialog)

    def retranslateUi(self, answerright_dialog):
        _translate = QtCore.QCoreApplication.translate
        answerright_dialog.setWindowTitle(_translate("answerright_dialog", "Dialog"))
        self.label.setText(_translate("answerright_dialog", "回答正确！"))
        self.pushButton.setText(_translate("answerright_dialog", "确定"))
