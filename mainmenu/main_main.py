from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import interface



class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_2.triggered.connect(app.quit)
        self.ui.action.triggered.connect(self.avtor)
        self.ui.action_4.triggered.connect(self.open_file)

    def avtor(self):
        self.ui.label.setText("ИП24-26")


    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "","All Files(*);;Text Files (*.txt)", options=options)
        if file_name:
            with open(file_name, 'r', encoding= "utf-8") as file:
                connect = file.read()
                self.ui.textEdit.setPlainText(connect)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())