from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QApplication,  QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class translator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):

        #labels
        polski = QLabel("Tekst po polsku:", self)
        kitku = QLabel("Tekst po kitkowemu:", self)

        #text area
        polskiTekst = QLineEdit()
        kitkuTekst = QLineEdit()

        #buttons
        trans = QPushButton("Tłumacz!", self)
        end = QPushButton("Koniec", self)

        layout = QGridLayout()
        layout.addWidget(polski, 0, 0)
        layout.addWidget(polskiTekst, 1,0)
        layout.addWidget(kitku, 2, 0)
        layout.addWidget(kitkuTekst, 3, 0)
        layout.addWidget(trans, 4, 1)
        layout.addWidget(end, 4, 2)

        self.setLayout(layout)
        self.resize(600, 480)
        self.setWindowTitle("- kitku translator -")
        self.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = translator()
    sys.exit(app.exec())
