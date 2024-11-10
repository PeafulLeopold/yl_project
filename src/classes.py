import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QColor, QTextCharFormat
from PyQt6 import QtCore

from data.py_items.config import EVENTS
from data.py_items.main_menu import Ui_MainMenu
from data.py_items.book import Ui_Book
from data.py_items.calendar_ import Ui_Calendar
from data.py_items.lessons import Ui_Lessons
from data.py_items.ancient_world import Ui_AncientWorld
from data.py_items.middle_ages import Ui_MiddleAges
from data.py_items.revival_era import Ui_RevivalEra
from data.py_items.new_era import Ui_NewEra
from data.py_items.twenty_century import Ui_TwentyCentury
from data.py_items.modern_world import Ui_ModernWorld
from data.py_items.quiz_introduction import Ui_QuizIntroduction


class Middle_Ages(QMainWindow, Ui_MiddleAges):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)
    
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


class Ancient_World(QMainWindow, Ui_AncientWorld):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)

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


class RevivalEra(QMainWindow, Ui_RevivalEra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)

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


class NewEra(QMainWindow, Ui_NewEra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)

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


class TwentyCentury(QMainWindow, Ui_TwentyCentury):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)

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


class ModernWorld(QMainWindow, Ui_ModernWorld):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)

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


class Lessons(QMainWindow, Ui_Lessons):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.return_button.clicked.connect(self.return_back)
        self.lessons_button.clicked.connect(self.open_lesson)
    
    def open_lesson(self):
        item_text = self.epochesbox.currentText()

        if item_text == 'Древний мир (до 500г н.э)':
            self.ancient_world_lesson = Ancient_World()
            self.ancient_world_lesson.show()
            self.hide()
        
        elif item_text == 'Средневековье (500-1500гг)':
            self.middle_ages_lesson = Middle_Ages()
            self.middle_ages_lesson.show()
            self.hide()
        
        elif item_text == 'Эпоха Возрождения и Реформации (1500-1700гг)':
            self.revival_era_lesson = RevivalEra()
            self.revival_era_lesson.show()
            self.hide()

        elif item_text == 'Новое время (1700-1900гг)':
            self.new_era_lesson = NewEra()
            self.new_era_lesson.show()
            self.hide()

        elif item_text == 'XX век (1900-2000гг)':
            self.twenty_century_lesson = TwentyCentury()
            self.twenty_century_lesson.show()
            self.hide()
        
        elif item_text == 'Современный мир (2000г - настоящее время)':
            self.modern_world_lesson = ModernWorld()
            self.modern_world_lesson.show()
            self.hide()
    
    def return_back(self):
        self.book = Book()
        self.book.show()
        self.hide()


class Calendar(QMainWindow, Ui_Calendar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.calendar.clicked.connect(self.show_event)
        self.return_button.clicked.connect(self.return_back) 
        self.format = QTextCharFormat()
        self.format.setBackground(QColor("red"))

        for event_date in EVENTS.keys():
            self.date = QtCore.QDate.fromString(event_date, 'yyyy-MM-dd')
            self.calendar.setDateTextFormat(self.date, self.format)
    
    def show_event(self):
        self.result.clear()
        selected_date = self.calendar.selectedDate()
        event = EVENTS.get(selected_date.toString('yyyy-MM-dd'), 'Информация об этой дате отсутствует.')
        self.result.insertPlainText(event)
    
    def return_back(self):
        self.book = Book()
        self.book.show()
        self.hide()


class QuizInroduction(QMainWindow, Ui_QuizIntroduction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.saw_button.clicked.connect(self.next_window)
        self.return_button.clicked.connect(self.return_back)
    
    def next_window(self):
        ...

    def return_back(self):
        self.new_menu = MainMenu()
        self.new_menu.show()
        self.hide()


class Book(QMainWindow, Ui_Book):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.return_page)
        self.calendar_button.clicked.connect(self.open_calendar)
        self.lesson_button.clicked.connect(self.open_lessons)
        
        self.back_button.setIcon(QIcon('data/icons/return.svg'))
    
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

class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.quiz_button.setIcon(QIcon('data/icons/quiz.svg'))
        self.help_button.setIcon(QIcon('data/icons/help.svg'))
        self.settings_button.setIcon(QIcon('data/icons/settings.svg'))
        self.book_button.setIcon(QIcon('data/icons/book.svg'))
        self.setStyleSheet('background-color: #FFE4B5; background-repeat: no-repeat; background-position: center')

        self.book_button.clicked.connect(self.open_book)
        self.quiz_button.clicked.connect(self.open_quiz)
    
    def open_quiz(self):
        self.quiz_introduction = QuizInroduction()
        self.quiz_introduction.show()
        self.hide()

    def open_book(self):
        self.book = Book()
        self.book.show()
        self.hide()