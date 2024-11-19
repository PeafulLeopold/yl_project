import random

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon, QColor, QTextCharFormat
from PyQt6 import QtCore

from py_items.config import EVENTS, CSV_DATA
from py_items.main_menu import Ui_MainMenu
from py_items.book import Ui_Book
from py_items.calendar_ import Ui_Calendar
from py_items.lessons import Ui_Lessons
from py_items.ancient_world import Ui_AncientWorld
from py_items.middle_ages import Ui_MiddleAges
from py_items.revival_era import Ui_RevivalEra
from py_items.new_era import Ui_NewEra
from py_items.twenty_century import Ui_TwentyCentury
from py_items.modern_world import Ui_ModernWorld
from py_items.quiz_introduction import Ui_QuizIntroduction
from py_items.ancient_first_lesson import Ui_AncientFirstLesson
from py_items.quiz_question import Ui_QuizQuestion
from py_items.quiz_result import Ui_QuizResult


QUESTION_NUMBER = 1
AMOUNT_OF_QUESTIONS = 1
LEVEL = ''
USED_LINES = []
CORRECT_ANSWERS = 0


class QuizResult(QMainWindow, Ui_QuizResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu_button.clicked.connect(self.open_menu)
        self.restart_button.clicked.connect(self.restart_quiz)
        self.setStyleSheet('background-color: #ffe4b5;')

        self.result_label.setText(f'{CORRECT_ANSWERS} из {AMOUNT_OF_QUESTIONS} баллов')
    
    def open_menu(self):
        global QUESTION_NUMBER
        global CORRECT_ANSWERS

        QUESTION_NUMBER = 1
        CORRECT_ANSWERS = 0

        self.menu_window = MainMenu()
        self.menu_window.show()
        self.hide()
    
    def restart_quiz(self):
        global QUESTION_NUMBER
        global CORRECT_ANSWERS

        self.new_quiz_window = QuizInroduction()
        self.new_quiz_window.show()
        self.hide()
        
        QUESTION_NUMBER = 1
        CORRECT_ANSWERS = 0

class QuizQuestion(QMainWindow, Ui_QuizQuestion):
    def __init__(self):
        global QUESTION_NUMBER
        global USED_LINES

        super().__init__()
        self.setupUi(self)
        self.end_button.clicked.connect(self.end_quiz)
        self.next_question_button.clicked.connect(self.open_next_question)
        self.setStyleSheet('background-color: #ffe4b5;')

        self.valid_lines = [line for line in CSV_DATA if line[1] == LEVEL and line not in USED_LINES]
        self.random_line = random.choice(self.valid_lines)
        self.question, self.difficulty = self.random_line[0], self.random_line[1]
        self.first_variant = self.random_line[2]
        self.second_variant = self.random_line[3]
        self.third_variant = self.random_line[4]
        self.fourth_variant = self.random_line[5]
        self.answer = self.random_line[6]

        self.question_number_label.setText(f'Вопрос №{QUESTION_NUMBER}')
        QUESTION_NUMBER += 1
        
        self.question_label.setText(self.question)
        self.first_variant_button.setText(self.first_variant)
        self.second_variant_button.setText(self.second_variant)
        self.third_variant_button.setText(self.third_variant)
        self.fourth_variant_button.setText(self.fourth_variant)

        self.first_variant_button.clicked.connect(self.check_answer)
        self.second_variant_button.clicked.connect(self.check_answer)
        self.third_variant_button.clicked.connect(self.check_answer)
        self.fourth_variant_button.clicked.connect(self.check_answer)

        self.buttons = [self.first_variant_button, self.second_variant_button,
                        self.third_variant_button, self.fourth_variant_button]
        
        USED_LINES.append(self.random_line)
    
    def check_answer(self):
        global CORRECT_ANSWERS

        given_answer = self.sender().text()

        if given_answer == self.answer:
            self.sender().setStyleSheet('background-color: green;')
            CORRECT_ANSWERS += 1
            
        else:
            self.sender().setStyleSheet('background-color: red;')

        for button in self.buttons:
            if button is not self.sender():
                button.setEnabled(False)

    def end_quiz(self):
        global QUESTION_NUMBER
        global CORRECT_ANSWERS

        QUESTION_NUMBER = 1
        CORRECT_ANSWERS = 0
        
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.hide()

    def open_next_question(self):
        if AMOUNT_OF_QUESTIONS >= QUESTION_NUMBER:
            self.next_question_window = QuizQuestion()
            self.next_question_window.show()
            self.hide()
        else:
            self.quiz_result_window = QuizResult()
            self.quiz_result_window.show()
            self.hide()


class AncientFirstLesson(QMainWindow, Ui_AncientFirstLesson):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.return_button.clicked.connect(self.return_back)
        self.next_lesson_button.clicked.connect(self.open_next_lesson)
        self.setStyleSheet('background-color: #ffe4b5;')

    def return_back(self):
        self.ancient_times = Ancient_World()
        self.ancient_times.show()
        self.hide()

    def open_next_lesson(self):
        ...


class Middle_Ages(QMainWindow, Ui_MiddleAges):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)
        self.setStyleSheet('background-color: #ffe4b5;')
    
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
        self.setStyleSheet('background-color: #ffe4b5;')

    def open_first_lesson(self):
        self.first_lesson_window = AncientFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
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
        self.setStyleSheet('background-color: #ffe4b5;')

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
        self.setStyleSheet('background-color: #ffe4b5;')

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
        self.setStyleSheet('background-color: #ffe4b5;')

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
        self.setStyleSheet('background-color: #ffe4b5;')

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
        self.setStyleSheet('background-color: #ffe4b5;')
    
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
        self.setStyleSheet('background-color: #ffe4b5;')

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
        self.next_button.clicked.connect(self.next_window)
        self.return_button.clicked.connect(self.return_back)
        self.setStyleSheet('background-color: #ffe4b5;')
    
    def next_window(self):
        global AMOUNT_OF_QUESTIONS
        global LEVEL

        AMOUNT_OF_QUESTIONS = int(self.amount_of_questions.text())
        LEVEL = self.chosen_level.currentText()

        self.quiz_question = QuizQuestion()
        self.quiz_question.show()
        self.hide()

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
        self.setStyleSheet('background-color: #ffe4b5;')
        
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

        self.book_button.clicked.connect(self.open_book)
        self.quiz_button.clicked.connect(self.open_quiz)
        self.setStyleSheet('background-color: #ffe4b5;')
    
    def open_quiz(self):
        self.quiz_introduction = QuizInroduction()
        self.quiz_introduction.show()
        self.hide()

    def open_book(self):
        self.book = Book()
        self.book.show()
        self.hide()