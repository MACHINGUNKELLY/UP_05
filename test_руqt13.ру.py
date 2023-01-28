from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class Window(QMainWindow):
   def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 250, 350, 200)
        self.setWindowTitle('Окно')
        self.button = QtWidgets.QPushButton(self)
        self.button.move(50, 50)
        self.button.setText('OK')
        self.button.setFixedWidth(70)
        self.button.clicked.connect(self.add_label)
   def add_label(self):
       print('Новая фраза')
def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    application()
