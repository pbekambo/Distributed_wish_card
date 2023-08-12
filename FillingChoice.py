import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot

class FromFile(QFileDialog):
    def __init__(self):
        super().__init__()

class FromPointer(QPixmap):
    def __init__(self):
        super().__init__()

class FromKeyboard(QTextEdit):
    def __init__(self):
        super().__init__()

class Choice(QWidget):
    def __init__(self):
        super().__init__()
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):    
        self.wish_fileButton     = QRadioButton("File")
        self.wish_pointerButton  = QRadioButton("Pointer")
        self.wish_keyboardButton = QRadioButton("Keyboard")
        self.wish_fileButton.setChecked(True)

        self.wish_menu_layout = QHBoxLayout()
        self.wish_menu_layout.addWidget(self.wish_fileButton)
        self.wish_menu_layout.addWidget(self.wish_pointerButton)
        self.wish_menu_layout.addWidget(self.wish_keyboardButton)
        self.wish_menu = QGroupBox()
        self.wish_menu.setLayout(self.wish_menu_layout)

        self.wish = QWidget()
        self.sign_fileButton     = QRadioButton("File")
        self.sign_pointerButton  = QRadioButton("Pointer")
        self.sign_fileButton.setChecked(True)
        
        self.sign_menu_layout = QHBoxLayout()
        self.sign_menu_layout.addWidget(self.sign_fileButton)
        self.sign_menu_layout.addWidget(self.sign_pointerButton)
        self.sign_menu = QGroupBox()
        self.sign_menu.setLayout(self.sign_menu_layout)

        self.sign = QWidget()

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.wish_menu)
        self.main_layout.addWidget(self.wish)
        self.main_layout.addWidget(self.sign_menu)
        self.main_layout.addWidget(self.sign)

        self.setLayout(self.main_layout)

        
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.choice = Choice()
        self.choice.setParent(self)
        self.show()
       

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec()) 




