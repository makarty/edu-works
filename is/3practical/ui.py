import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import inf3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.outputB = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputB.setObjectName("outputB")
        self.verticalLayout.addWidget(self.outputB)

        self.encodeB = QtWidgets.QPushButton(self.centralwidget)
        self.encodeB.setObjectName("encodeB")
        self.verticalLayout.addWidget(self.encodeB)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.encodeB.clicked.connect(self.encode_list)

        self.BoxList = QtWidgets.QComboBox(self.centralwidget)
        self.BoxList.setObjectName("BoxList")
        self.horizontalLayout.addWidget(self.BoxList)
        self.BoxList.activated.connect(self.decode)
        self.BoxList.setMinimumSize(200,25)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
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
        self.encodeB.setText(_translate("MainWindow", "расшифровать"))

    def encode_list(self):
        pk = inf3.applic()
        print(pk)
        for i in pk:
            self.BoxList.addItem(i)

    def decode(self):
        self.outputB.setText(inf3.enc(self.BoxList.currentText()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
