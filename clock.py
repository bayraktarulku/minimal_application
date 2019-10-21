import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLCDNumber, QRadioButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from time import strftime

var = True


class Main(QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.initUI()

    def initUI(self):

        timer = QTimer(self)
        timer.timeout.connect(self.Time)
        timer.start(10)

        self.lcd = QLCDNumber(self)
        self.lcd.resize(250, 100)

        self.lcd.move(0, 30)
        self.lcd.display(strftime('%H' + ':' + '%M'))

        self.r1 = QRadioButton('Hide seconds', self)
        self.r1.move(10, 0)
        self.r2 = QRadioButton('Show seconds', self)
        self.r2.move(110, 0)

        self.r1.toggled.connect(self.woSecs)
        self.r2.toggled.connect(self.wSecs)

        self.setGeometry(300, 300, 250, 130)
        self.setWindowTitle('Clock')
        self.setWindowIcon(QIcon(''))
        self.show()

    def Time(self):
        global var
        if var == True:
            self.lcd.display(strftime('%H' + ':' + '%M'))
        elif var == False:
            self.lcd.display(strftime('%H' + ':' + '%M' + ':' + '%S'))

    def wSecs(self):
        global var
        var = False

        self.resize(375, 130)
        self.lcd.resize(375, 100)
        self.lcd.setDigitCount(8)

    def woSecs(self):
        global var
        var = True
        self.resize(250, 130)
        self.lcd.resize(250, 100)
        self.lcd.setDigitCount(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
