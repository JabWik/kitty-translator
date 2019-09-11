from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QApplication,  QWidget, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class translator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):

        #labels
        polish = QLabel("Tekst po polsku:", self)
        kitty = QLabel("Tekst po kitkowemu:", self)

        #text area
        polishText = QPlainTextEdit(self)
        polishText.insertPlainText("Adanos karmi nas swoją świętą mocą...")
        polishText.resize(300,480)


        kittyText = QPlainTextEdit(self)

        #buttons
        trans = QPushButton("Translate!", self)
        end = QPushButton("Exit", self)

        layout = QGridLayout()
        layout.addWidget(polish, 0, 0)
        layout.addWidget(polishText, 1,0)
        layout.addWidget(kitty, 2, 0)
        layout.addWidget(kittyText, 3, 0)
        layout.addWidget(trans, 4, 0)
        layout.addWidget(end, 4, 2)

        self.setLayout(layout)
        self.resize(600, 480)
        self.setWindowTitle("- kitku translator v.1.0 -")
        self.setWindowIcon(QIcon('cat-icon.png'))
        self.show()





if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = translator()
    sys.exit(app.exec())
