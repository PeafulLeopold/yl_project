from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from py_items.design_modern_world import Ui_ModernWorld
from lessons import Lessons


class ModernWorld(QMainWindow, Ui_ModernWorld):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)
        self.setStyleSheet('background-color: #ffe4b5')

    def open_first_lesson(self):
        ...
    
    def open_second_lesson(self):
        ...
    
    def open_third_lesson(self):
        ...
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()