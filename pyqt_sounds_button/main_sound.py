# from PyQt5 import QtWidgets,QtMultimedia, QtCore
# import sounds_bober, os
# class MyWindow ( QtWidgets.QWidget):
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
#         self.ui = sounds_bober.Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.sndEffect = QtMultimedia.QSoundEffect()
#         self.ui.pushButton.clicked.connect(self.sound1)
#         self.ui.pushButton_2.clicked.connect(self.sound2)

#     def sound1(self):
#         fn = QtCore.QUrl.fromLocalFile(os.path.abspath("net.wav"))
#         self.sndEffect.setSource(fn)
#         self.sndEffect.setVolume(1)
#         self.sndEffect.play()

    
#     def sound2(self):
#         fn = QtCore.QUrl.fromLocalFile(os.path.abspath("2.wav"))
#         self.sndEffect.setSource(fn)
#         self.sndEffect.setVolume(0,5)
#         self.sndEffect.play()

    
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())




 
from PyQt5 import QtCore, QtWidgets, QtMultimedia 
import sys, os 
 
class MyWindow(QtWidgets.QWidget): 
    def __init__(self, parent=None): 
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window | 
                                   QtCore.Qt.MSWindowsFixedSizeDialogHint) 
        self.setWindowTitle("Звуковые эффекты") 
         
# Инициализируем подсистему вывода звуковых эффектов 
        self.sndEffect = QtMultimedia.QSoundEffect() 
        self.sndEffect.setVolume(1) 
         
# Задаем файл-источник 
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("2.wav")) 
        self.sndEffect.setSource(fn) 
        self.sndEffect.loopsRemainingChanged.connect(self.showCount) 
        self.sndEffect.playingChanged.connect(self.clearCount) 
        vbox = QtWidgets.QVBoxLayout() 
         
# Создаем кнопки для запуска воспроизведения звука 
        lblPlay = QtWidgets.QLabel("Воспроизвести...") 
        vbox.addWidget(lblPlay) 
        btnOnce = QtWidgets.QPushButton("...&один раз") 
        btnOnce.clicked.connect(self.playOnce) 
        vbox.addWidget(btnOnce) 
        btnTen = QtWidgets.QPushButton("...&десять раз") 
        btnTen.clicked.connect(self.playTen) 
        vbox.addWidget(btnTen) 
        btnInfinite = QtWidgets.QPushButton( 
            "...&бесконечное количество раз") 
        btnInfinite.clicked.connect(self.playInfinite) 
        vbox.addWidget(btnInfinite) 
        btnStop = QtWidgets.QPushButton("&Стоп") 
        btnStop.clicked.connect(self.sndEffect.stop) 
        vbox.addWidget(btnStop) 
        self.lblStatus = QtWidgets.QLabel("") 
        vbox.addWidget(self.lblStatus) 
        self.setLayout(vbox) 
        self.resize(1000, 500) 
 
    def playOnce(self): 
        self.sndEffect.setLoopCount(1) 
        self.sndEffect.play() 
 
    def playTen(self): 
        self.sndEffect.setLoopCount(10) 
        self.sndEffect.play() 
 
    def playInfinite(self): 
        self.sndEffect.setLoopCount(QtMultimedia.QSoundEffect.Infinite) 
        self.sndEffect.play() 
 
    # Выводим количество повторений воспроизведения эффекта 
    def showCount(self): 
        self.lblStatus.setText("Воспроизведено " + 
                               str(self.sndEffect.loopCount() -                                self.sndEffect.loopsRemaining()) + " раз") 
 
    # Если воспроизведение закончено, очищаем выведенное ранее 
    # количество повторений эффекта 
    def clearCount(self): 
        if not self.sndEffect.isPlaying(): 
            self.lblStatus.setText("") 
 
app = QtWidgets.QApplication(sys.argv) 
window = MyWindow() 
window.show() 
sys.exit(app.exec_())