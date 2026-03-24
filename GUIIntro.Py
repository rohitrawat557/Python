import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool first GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("profile_pic.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


# git init
# git remote add origin https://github.com/username/repo-name.git
# git add .  
# git commit -m "Your commit message"
# git push origin main
# git push -u origin main