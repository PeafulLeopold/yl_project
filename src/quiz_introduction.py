from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from py_items.design_quiz_introduction import Ui_QuizIntroduction
from main_menu import MainMenu

class QuizInroduction(QMainWindow, Ui_QuizIntroduction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.saw_button.clicked.connect(self.next_window)
        self.return_button.clicked.connect(self.return_back)
        self.setStyleSheet('background-color: #ffe4b5')
    
    def next_window(self):
        ...

    def return_back(self):
        self.new_menu = MainMenu()
        self.new_menu.show()
        self.hide()