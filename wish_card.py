#from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, pyqtSlot

import sys

class Wish(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        #self.left = 10
        #self.top = 10
        #self.width = 400
        #self.height = 140
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)

        self.btn_close = QPushButton("Exit without save")
        self.btn_new = QPushButton("Save")
        self.wish = QTextEdit()
        self.signature = QFileDialog()
        self.form_layout = QFormLayout()
        self.form_layout.addRow("Wish", self.wish)
        self.form_layout.addRow("Signature", self.signature)
        self.form_layout.addRow("", self.btn_close)
        self.form_layout.addRow("", self.btn_new)
        self.setLayout(self.form_layout)
    
        # Create textbox
        #self.textbox = QTextEdit(self)
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)

        #self.signarure = QFileDialog.getOpenFileName(self,'Open file','c:\\', "Image files (*.jpg *.gif)")
        
        # Create a button in the window
        #self.button = QPushButton('Show text', self)
        #self.button.move(20,80)
        
        # connect button to function on_click
        #self.button.clicked.connect(self.on_click)
        self.show()
    
    #@pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Wish Card"
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 500
        
        self.mdi = QMdiArea()
        self.mdi.setFixedSize(1000, 400)
         # Create a button in the window
        # self.button = QPushButton('Write your message and sign card', self)
        self.button = QLabel('Write your message and sign card', self)
        self.button.setWordWrap(True)
        self.button.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.button.mousePressEvent = self.on_click
        # self.button.move(20,80)
        self.button.move(380,280)
                
        # connect button to function on_click
        #self.button.clicked.connect(self.on_click)
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()     
      
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,  5, Qt.SolidLine))
        painter.drawRect(40, 40, 400, 200)
       

    def on_click(self, event):
        self.wish = Wish()
       
  
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec()) 
  
