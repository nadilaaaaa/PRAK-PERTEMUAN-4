import sys
from PyQt5.QtWidgets import QApplication

from Latihan2 import*

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = Latihan2()
    form.show()

    a.exec_()
