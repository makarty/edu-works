from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cipher import *


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(15, 180, 200, 50))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(215, 180, 200, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        self.resultLabel = QtWidgets.QLabel(self.centralwidget)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(15, 100, 400, 50))
        self.textEdit.setObjectName("textEdit")

        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.decrypt)

        self.protect = QtWidgets.QCheckBox(self.centralwidget)
        self.protect.setGeometry(QtCore.QRect(15, 160, 400, 15))
        self.protect.setText("Повысить криптостойкость")

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
        rep = text.replace(' ', 'а')
        if not rep.isalpha():
            message = QMessageBox(self.centralwidget)
            message.setWindowTitle("Ошибка")
            message.setText("Недопустимые символы")
            message.setIcon(QMessageBox.Critical)
            message.show()
            return
        cl = MirabeauCipher()
        if self.protect.isChecked():
            enc = str(cl.encryption_2x(text))
        else:
            enc = str(cl.encryption(text))
        self.resultLabel.setGeometry(QtCore.QRect(430, 90, 500, 50))
        self.resultLabel.setStyleSheet("font-size: 19px")
        self.resultLabel.setText("Результат: " + enc)

    def decrypt(self):
        text = self.textEdit.toPlainText()
        text = text.split()
        for i in range(len(text)):
            digit = text[i].replace('.', '')
            if not digit.isdigit():
                message = QMessageBox(self.centralwidget)
                message.setWindowTitle("Ошибка")
                message.setText("Недопустимые символы")
                message.setIcon(QMessageBox.Critical)
                message.show()
                return
            text[i] = float(text[i])
        cl = MirabeauCipher()
        try:
            if self.protect.isChecked():
                dec = cl.decryption_2x(text)
                dec = cl.decryption(dec)
            else:
                dec = cl.decryption(text)
        except IndexError:
            message = QMessageBox(self.centralwidget)
            message.setWindowTitle("Ошибка")
            message.setText("Введена неверная последовательность")
            message.setIcon(QMessageBox.Critical)
            message.show()
            return
        self.resultLabel.setGeometry(QtCore.QRect(430, 90, 400, 50))
        self.resultLabel.setStyleSheet("font-size: 19px")
        self.resultLabel.setText("Результат: " + dec)
