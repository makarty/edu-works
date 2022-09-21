from PyQt5 import QtCore, QtWidgets
from cipher import *


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(15, 175, 200, 50))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(215, 175, 200, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(15, 100, 400, 70))
        self.textEdit.setObjectName("textEdit")
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.decrypt)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 49, 400, 51))
        self.label.setStyleSheet("font-size: 11px")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
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
        self.pushButton.setText(_translate("MainWindow", "Зашифровать"))
        self.pushButton_2.setText(_translate("MainWindow", "Расшифровать"))
        self.label.setText(_translate("MainWindow", "Введите строку, которую необходимо зашифровать или расшифровать"))

    def encrypt(self):
        text = self.textEdit.toPlainText()
        if not text.isalpha():
            return
        cl = MirabeauCipher()
        cl.encryption(text)

    def decrypt(self):
        text = self.textEdit.toPlainText()
        text = text.split()
        for i in range(len(text)):
            digit = text[i].replace('.', '')
            if not digit.isdigit():
                return
            text[i] = float(text[i])
        cl = MirabeauCipher()
        cl.decryption(text)
