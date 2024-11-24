from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from py_items.design_book import Ui_Book
from main_menu import MainMenu
from calendar import Calendar
from lessons import Lessons

class Book(QMainWindow, Ui_Book):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.return_page)
        self.calendar_button.clicked.connect(self.open_calendar)
        self.lesson_button.clicked.connect(self.open_lessons)
        
        self.back_button.setIcon(QIcon('data/icons/return.svg'))
        self.setStyleSheet('background-color: #ffe4b5')
    
    def return_page(self):
        self.menu = MainMenu()
        self.menu.show()
        self.hide()

    def open_calendar(self):
        self.new_calendar = Calendar()
        self.new_calendar.show()
        self.hide()
    
    def open_lessons(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()
