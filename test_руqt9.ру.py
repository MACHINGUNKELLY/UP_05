from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
def application():
 app = QApplication(sys.argv)
 window = QMainWindow()
 window.setGeometry(300, 250, 350, 200)
 window.setWindowTitle('Окно')
 window_text = QtWidgets.QLabel(window)
 window_text.setText('Первая запись')
 window_text.move(10, 10)
 window_text.adjustSize()
 window.show()
 sys.exit(app.exec_())
if __name__ == '__main__':
 application()
