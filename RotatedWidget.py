import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def getText():
    noforcepoint
def getSeal():
    noforcepoint

def main():
    import sys

    app = QApplication(sys.argv)

    pix = QPixmap('Signature.jpeg')
    qp = QPainter(pix)
    pen = QPen(Qt.red, 3)
    qp.setPen(pen)
    '''qp.drawLine(10, 10, 50, 50)'''

    qp.drawText(pix.rect(), Qt.AlignTop, "BlaBla")

    qp.end()

    label = QLabel(alignment=Qt.AlignCenter)
    label.setPixmap(pix)
    '''label.setWindowTitle("BlaBla")'''

    graphicsview = QGraphicsView()
    scene = QGraphicsScene(graphicsview)
    graphicsview.setScene(scene)

    proxy = QGraphicsProxyWidget()
    proxy.setWidget(label)
    proxy.setTransformOriginPoint(proxy.boundingRect().center())
    scene.addItem(proxy)

    slider = QSlider(minimum=0, maximum=359, orientation=Qt.Horizontal)
    slider.valueChanged.connect(proxy.setRotation)

    label_text = QLabel(
        "{}°".format(slider.value()), alignment=Qt.AlignCenter
    )
    slider.valueChanged.connect(
        lambda value: label_text.setText("{}°".format(slider.value()))
    )

    slider.setValue(45)

    w = QWidget()
    lay = QVBoxLayout(w)
    lay.addWidget(graphicsview)
    lay.addWidget(slider)
    lay.addWidget(label_text)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()