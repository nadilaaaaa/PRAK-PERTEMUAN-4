from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

class About(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(180,120)
        self.move(50,50)
        self.setWindowTitle('About')

        self.label1 = QLabel('Dibuat oleh Tim RPL')
        self.label2 = QLabel('Versi 1.0')
        self.label3 = QLabel('Copyright@2019')
        self.label1.move(40,30)
        self.label2.move(40,40)
        self.label3.move(40,50)
        self.label1.setParent(self)
        self.label2.setParent(self)
        self.label3.setParent(self)

        self.button = QPushButton('OK')
        self.button.move(80,70)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
