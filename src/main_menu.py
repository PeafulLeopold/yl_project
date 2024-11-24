from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from py_items.main_menu import Ui_MainMenu
from quiz_introduction import QuizInroduction
from book import Book


class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.quiz_button.setIcon(QIcon('data/icons/quiz.svg'))
        self.help_button.setIcon(QIcon('data/icons/help.svg'))
        self.settings_button.setIcon(QIcon('data/icons/settings.svg'))
        self.book_button.setIcon(QIcon('data/icons/book.svg'))

        self.book_button.clicked.connect(self.open_book)
        self.quiz_button.clicked.connect(self.open_quiz)

        self.setStyleSheet('background-color: #ffe4b5')
        
    def open_quiz(self):
        self.quiz_introduction = QuizInroduction()
        self.quiz_introduction.show()
        self.hide()

    def open_book(self):
        self.book = Book()
        self.book.show()
        self.hide()