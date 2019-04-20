import sys
from PyQt5.QtWidgets import QApplication

from MultipleForm import *

if __name__=='__main__':
        a = QApplication(sys.argv)

        minform = MultipleForm()
        minform.show()
        a.exec_()
