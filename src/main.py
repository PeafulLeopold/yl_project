import sys
from PyQt6.QtWidgets import QApplication
from src.classes import MainMenu


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = MainMenu()
    menu.show()
    sys.exit(app.exec())