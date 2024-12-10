from PyQt5 import QtWidgets
import thisbiba, thisboba


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = thisbiba.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open)


    def open(self):
        vt.show()




class TwoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = thisboba.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open2)


    def open2(self):
        a = float(self.ui.lineEdit.text())
        self.ui.label.setText(str(a+(a*0.15)))




if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    vt = TwoWindow()
    window.show()
    sys.exit(app.exec_())