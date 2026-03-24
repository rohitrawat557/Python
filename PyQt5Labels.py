from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:blue;"
                            "background-color:yellow;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")
        
        # label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()