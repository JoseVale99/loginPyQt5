from PyQt5.QtWidgets import (QMainWindow,
     QDesktopWidget)

import sys
from view.login import Ui_MainWindow


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.login = Ui_MainWindow()      
        self.login.setupUi(self)
           
        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))
        