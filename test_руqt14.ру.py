from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class Window(QMainWindow):
    def __init__(self):
      super(Window, self).__init__()
      self.setGeometry(300, 250, 350, 200)
      self.setWindowTitle('Окно')
      self.window_text = QtWidgets.QLabel(self)
      self.window_text.setText('Первая запись')
      self.window_text.move(10, 10)
      self.window_text.adjustSize()
def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    application()
