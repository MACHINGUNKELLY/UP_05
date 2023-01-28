from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(300, 250, 350, 200)
window.setWindowTitle('Окно')
window.show()
sys.exit(app.exec_())
