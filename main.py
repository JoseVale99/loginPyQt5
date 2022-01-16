from PyQt5.QtWidgets import (QApplication)
from controller.loginController import Login
from style.style import style
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.setStyleSheet(style)
    login.show()
    sys.exit(app.exec_())