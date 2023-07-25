from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, pyqtSlot, QPoint

import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 1000, 800)
        self.setWindowTitle('Painter')
        self.background_color = '#242423'
        layout = QVBoxLayout(self)
        # create view 
        view = View()
        scene = QGraphicsScene()
        scene.setBackgroundBrush(QBrush(QColor(self.background_color)))
        scene.setSceneRect(0, 0, 150, 150)
        # add view to layout
        layout.addWidget(view)
        # add scene to view
        view.setScene(scene)
        
class View(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.pen = QPen()
        self.pen.setColor(Qt.red)
        self.start = QPoint()
        self.end = QPoint()
        self.setMouseTracking(True)
        self.mousePreseed = False
        self.rect, self.line = None, None

    def drawShape(self):
        if self.start.isNull() or self.end.isNull():
            return
        if self.start.x() == self.end.x() and self.start.y() == self.end.y():
            return
        elif abs(self.end.x() - self.start.x()) < 20 or abs(self.end.y() - self.start.y()) < 20:
            if self.rect != None:
                self.scene().removeItem(self.rect)
                self.rect = None
            if abs(self.end.y() - self.start.y()) < 20:
                # draw vertical line
                if self.line != None:
                    self.line.setLine(self.start.x(), self.start.y(), self.end.x(), self.start.y())
                else:
                    self.line = self.scene().addLine(self.start.x(), self.start.y(), self.end.x(), self.start.y(), self.pen)
            else:
                # draw horizontal line
                if self.line != None:
                    self.line.setLine(self.start.x(), self.start.y(), self.start.x(), self.end.y())
                else:
                    self.line = self.scene().addLine(self.start.x(), self.start.y(), self.start.x(), self.end.y(), self.pen)                    
        else:
            if self.line != None:
                self.scene().removeItem(self.line)
                self.line = None

            width = abs(self.start.x() - self.end.x())
            height = abs(self.start.y() - self.end.y())
            if self.rect == None:
                self.rect = self.scene().addRect(min(self.start.x(), self.end.x()), min(self.start.y(), self.end.y()), width, height, self.pen)
            else:
                self.rect.setRect(min(self.start.x(), self.end.x()), min(self.start.y(), self.end.y()), width, height)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePreseed = True
            self.start = self.mapToScene(event.pos())
           
    
    def mouseMoveEvent(self,event):
        if event.buttons() & Qt.LeftButton & self.mousePreseed:
            self.end = self.mapToScene(event.pos())
            self.drawShape()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.mousePreseed:
            self.mousePreseed = False
            self.drawShape()
            self.start, self.end = QPoint(), QPoint()
            self.rect, self.line = None, None

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()