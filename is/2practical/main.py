# This is a sample Python script.
# import RSA
# import degree
# import numpy
# import sympy
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import design


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = design.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
