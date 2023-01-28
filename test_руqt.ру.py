from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
def add_label():
 print('Hello world')
def application():
 app = QApplication(sys.argv)
 window = QMainWindow()
 window.setGeometry(300, 250, 350, 200)
 window.setWindowTitle('Окно')
 button = QtWidgets.QPushButton(window)
 button.move(50, 50)
 button.setText('OK')
 button.setFixedWidth(70)
 button.clicked.connect(add_label)
 window.show()
 sys.exit(app.exec_())
if __name__ == '__main__':
 application()
