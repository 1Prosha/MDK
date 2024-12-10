from PyQt5 import QtWidgets, QtCore
import time
import piv, pav


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = piv.Ui_Form()
        self.ui.setupUi(self)




class Zastavka(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = pav.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.doAction)



    def doAction(self):
        a = 0
        while a < 100:
            a += 20
            time.sleep(1)
            self.ui.progressBar.setVaule(a)
        else:
            zas.close()
            window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowFlag(QtCore.Qt.Drawer)
    zas = Zastavka()
    zas.setWindowFlag(QtCore.Qt.SplashScreen)
    zas.show()
    # zas.doAction()
    sys.exit(app.exec_())