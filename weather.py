from PyQt5.QtWidgets import (
    QApplication, QWidget, QComboBox)
from PyQt5.QtCore import QRect
from pprint import pprint
import requests
import sys

lists_of_cities = [{'id': 1, 'name': 'İstanbul'},
                   {'id': 2, 'name': 'Ankara'},
                   {'id': 3, 'name': 'İzmir'},
                   {'id': 4, 'name': 'Adana'},
                   {'id': 5, 'name': 'Adıyaman'},
                   {'id': 6, 'name': 'Afyon'},
                   {'id': 7, 'name': 'Ağrı'},
                   {'id': 8, 'name': 'Aksaray'},
                   {'id': 9, 'name': 'Amasya'},
                   {'id': 10, 'name': 'Antalya'},
                   {'id': 11, 'name': 'Ardahan'},
                   {'id': 12, 'name': 'Artvin'},
                   {'id': 13, 'name': 'Aydın'},
                   {'id': 14, 'name': 'Balıkesir'},
                   {'id': 15, 'name': 'Bartın'},
                   {'id': 16, 'name': 'Batman'},
                   {'id': 17, 'name': 'Bayburt'},
                   {'id': 18, 'name': 'Bilecik'},
                   {'id': 19, 'name': 'Bingöl'},
                   {'id': 20, 'name': 'Bitlis'},
                   {'id': 21, 'name': 'Bolu'},
                   {'id': 22, 'name': 'Burdur'},
                   {'id': 23, 'name': 'Bursa'},
                   {'id': 24, 'name': 'Çanakkale'},
                   {'id': 25, 'name': 'Çankırı'},
                   {'id': 26, 'name': 'Çorum'},
                   {'id': 27, 'name': 'Denizli'},
                   {'id': 28, 'name': 'Diyarbakır'},
                   {'id': 29, 'name': 'Edirne'},
                   {'id': 30, 'name': 'Elazığ'},
                   {'id': 31, 'name': 'Erzincan'},
                   {'id': 32, 'name': 'Erzurum'},
                   {'id': 33, 'name': 'Eskişehir'},
                   {'id': 34, 'name': 'Gaziantep'},
                   {'id': 35, 'name': 'Giresun'},
                   {'id': 36, 'name': 'Gümüşhane'},
                   {'id': 37, 'name': 'Hakkari'},
                   {'id': 38, 'name': 'Hatay'},
                   {'id': 39, 'name': 'Mersin'},
                   {'id': 40, 'name': 'Iğdır'},
                   {'id': 41, 'name': 'Isparta'},
                   {'id': 42, 'name': 'Kahramanmaraş'},
                   {'id': 43, 'name': 'Karabük'},
                   {'id': 44, 'name': 'Karaman'},
                   {'id': 45, 'name': 'Kars'},
                   {'id': 46, 'name': 'Kastamonu'},
                   {'id': 47, 'name': 'Kayseri'},
                   {'id': 48, 'name': 'Kırıkkale'},
                   {'id': 49, 'name': 'Kırklareli'},
                   {'id': 50, 'name': 'Kırşehir'},
                   {'id': 51, 'name': 'Kilis'},
                   {'id': 52, 'name': 'Kocaeli'},
                   {'id': 53, 'name': 'Konya'},
                   {'id': 54, 'name': 'Kütahya'},
                   {'id': 55, 'name': 'Malatya'},
                   {'id': 56, 'name': 'Manisa'},
                   {'id': 57, 'name': 'Mardin'},
                   {'id': 58, 'name': 'Muğla'},
                   {'id': 59, 'name': 'Muş'},
                   {'id': 60, 'name': 'Nevşehir'},
                   {'id': 61, 'name': 'Niğde'},
                   {'id': 62, 'name': 'Ordu'},
                   {'id': 63, 'name': 'Osmaniye'},
                   {'id': 64, 'name': 'Rize'},
                   {'id': 65, 'name': 'Sakarya'},
                   {'id': 66, 'name': 'Samsun'},
                   {'id': 67, 'name': 'Siirt'},
                   {'id': 68, 'name': 'Sinop'},
                   {'id': 69, 'name': 'Sivas'},
                   {'id': 70, 'name': 'Şanlıurfa'},
                   {'id': 71, 'name': 'Şırnak'},
                   {'id': 72, 'name': 'Tekirdağ'},
                   {'id': 73, 'name': 'Tokat'},
                   {'id': 74, 'name': 'Trabzon'},
                   {'id': 75, 'name': 'Tunceli'},
                   {'id': 76, 'name': 'Uşak'},
                   {'id': 77, 'name': 'Van'},
                   {'id': 78, 'name': 'Yalova'},
                   {'id': 79, 'name': 'Yozgat'},
                   {'id': 80, 'name': 'Zonguldak'}]


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet('QWidget { background: #fff }')
        self.setFixedSize(300, 300)
        self.setWindowTitle('Application')
        self.createCombobox()
        self.show()

    def createCombobox(self):
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(40, 40, 100, 31))
        self.comboBox.setObjectName(('comboBox'))
        for city in lists_of_cities:
            self.comboBox.addItem(city['name'])
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

    def get_weather(self):

        # r = requests.get(
        #     'http://api.wunderground.com/api/xxxx/conditions/q/Turkey/Istanbul.json')
        # pprint(r.json())
        pass

    def selectionchange(self, i):
        print('Current index: ', i, 'Selected city: ',
              self.comboBox.currentText())


def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
