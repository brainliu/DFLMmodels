# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(482, 354)
        self.centralWidget = QtWidgets.QWidget(form)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 120, 261, 87))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        form.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(form)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 482, 26))
        self.menuBar.setObjectName("menuBar")
        form.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(form)
        self.mainToolBar.setObjectName("mainToolBar")
        form.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(form)
        self.statusBar.setObjectName("statusBar")
        form.setStatusBar(self.statusBar)

        self.retranslateUi(form)
        self.pushButton.clicked.connect(form.hello)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "form"))
        self.textEdit.setHtml(_translate("form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello</p></body></html>"))
        self.pushButton.setText(_translate("form", "hello"))

