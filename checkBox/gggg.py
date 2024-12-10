from PyQt5 import QtWidgets
import ggg

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ggg.Ui_Form()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.clear)
        self.ui.pushButton.clicked.connect(self.cheker)
        self.ui.checkBox.stateChanged.connect(self.cheker)



    def cheker(self):
        if self.ui.checkBox.isChecked():
            self.ui.label.setText("привет")
        else:
            self.ui.label.clear()

        if self.ui.checkBox.isChecked and self.ui.checkBox_2.isChecked():
            self.ui.label_2.setText("привет x2")

        else:
            self.ui.label_2.clear()

        if self.ui.checkBox_2.isChecked():
            self.ui.label_3.setText("пока")


        else:
            self.ui.label_3.clear()

        


        if self.ui.checkBox.isChecked and self.ui.checkBox_2.isChecked and self.ui.checkBox_3.isChecked():
            self.ui.label.setText("ulta")
            self.ui.label_2.setText("ulta")
            self.ui.label_3.setText("ulta")


        else:
            self.ui.lineEdit.setText("chose your answer")


    def clear(self):
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())