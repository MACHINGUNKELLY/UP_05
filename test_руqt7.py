import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
QPushButton

def add_label():
    print('Hello world')

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Окно')

    button = QPushButton(w)
    button.move(50, 50)
    button.setText('OK')
    button.setFixedWidth(70)
    button.clicked.connect(add_label)

    w.show()

    sys.exit(app.exec_())
