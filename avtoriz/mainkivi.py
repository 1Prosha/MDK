from PyQt5 import QtWidgets
import untitled, untitled2


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = untitled.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open)


    def open(self):
        vt.show()




class TwoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = untitled2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_glav)
        # self.ui.pushButton_2.clicked.connect(self.password)


    def open_glav(self):
        if self.ui.lineEdit.text() == "Admin" and self.ui.lineEdit_2.text() == "Admin":
            window.show()
            # password.close()
        elif self.ui.lineEdit.text() == "":
            self.ui.label.setText("Введите логин")
        elif self.ui.lineEdit_2.text() == "":
            self.ui.label.setText("Введите пароль")
        else:
            self.ui.label.setText("Неправильно")
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()

        # def password(self):
        #     password.close()


if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    vt = TwoWindow()
    window.show()
    sys.exit(app.exec_())