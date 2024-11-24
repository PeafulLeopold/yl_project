import random

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout
from PyQt6.QtGui import QIcon, QColor, QTextCharFormat, QPixmap, QIcon
from PyQt6 import QtCore, QtWidgets

from py_items.config import EVENTS, CSV_DATA, change_on_dark_theme, MODERN_WORLD_1_FORMATTED
from py_items.config import TWENTY_CENTURY_1_FORMATTED, TWENTY_CENTURY_2_FORMATTED, NEW_ERA_1_FORMATTED
from py_items.config import REVIVAL_1_FORMATTED, REVIVAL_2_FORMATTED, MIDDLE_AGES_1_FORMATTED, MIDDLE_AGES_2_FORMATTED
from py_items.config import ANCIENT_1_FORMMATED, ANCIENT_2_FORMMATED, ANCIENT_3_FORMMATED

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
from py_items.quiz_question import Ui_QuizQuestion
from py_items.quiz_result import Ui_QuizResult
from py_items.settings import Ui_Settings
from py_items.lesson import Ui_Lesson
from py_items.help import Ui_Help


THEME = 'light'


QUESTION_NUMBER = 1
AMOUNT_OF_QUESTIONS = 1
LEVEL = ''
USED_LINES = []
CORRECT_ANSWERS = 0


class Lesson(QMainWindow, Ui_Lesson):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet('background-color: #ffe4b5;')
        self.return_button.clicked.connect(self.return_back)
        self.next_lesson_button.clicked.connect(self.open_next_lesson)
        self.previous_lesson_button.clicked.connect(self.open_previous_lesson)
        
        self.fourth_photo.setScaledContents(True)
        self.second_photo.setScaledContents(True)
        self.first_photo.setScaledContents(True)
        self.third_photo.setScaledContents(True)

        self.next_lesson_button.setIcon(QIcon('data/icons/next.svg'))
        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.previous_lesson_button.setIcon(QIcon('data/icons/previous.svg'))

        self.widgets = [self.heading_label, self.first_label, self.second_label,
                        self.third_label, self.fourth_label, self.return_button,
                        self.next_lesson_button, self.previous_lesson_button]
        
        if THEME == 'dark':
            change_on_dark_theme(self)

            self.main_text.setStyleSheet("color: white; background-color: #151719;")

    

class ModernWorldFirstLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(MODERN_WORLD_1_FORMATTED)
        self.heading_label.setText('Развитие технологий')
    
    def open_next_lesson(self):
        self.first_lesson_window = AncientFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = TwentyCenturySecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = ModernWorld()
        self.back.show()
        self.hide()


class TwentyCenturySecondLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(TWENTY_CENTURY_2_FORMATTED)
        self.heading_label.setText('Вторая Мировая Война')
        
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/ger_pol.webp'))
        self.first_label.setText('Немецкая атака на Польшу')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/perl.webp'))
        self.second_label.setText('Атака на Перл-Харбор')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/england_fight.webp'))
        self.fourth_label.setText('Битва за Англию')

    def open_next_lesson(self):
        self.first_lesson_window = ModernWorldFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = TwentyCenturyFirstLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = TwentyCentury()
        self.back.show()
        self.hide()


class TwentyCenturyFirstLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(TWENTY_CENTURY_1_FORMATTED)
        self.heading_label.setText('Первая Мировая Война')
        
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/marna.webp'))
        self.first_label.setText('Битва близ реки Марны')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/somma.webp'))
        self.second_label.setText('Битва близ реки Соммы')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/peaceful_meeting.webp'))
        self.fourth_label.setText('Компьерский договор')

        self.third_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/gal.webp'))
        self.third_label.setText('Галлипольская операция')
    
    def open_next_lesson(self):
        self.first_lesson_window = TwentyCenturySecondLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = NewEraFirstLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = TwentyCentury()
        self.back.show()
        self.hide()


class NewEraFirstLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(NEW_ERA_1_FORMATTED)
        self.heading_label.setText('Просвещение и его идеи')
    
    def open_next_lesson(self):
        self.first_lesson_window = TwentyCenturyFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = RevivalSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = NewEra()
        self.back.show()
        self.hide()


class RevivalSecondLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(REVIVAL_2_FORMATTED)
        self.heading_label.setText('Появление колонизации и глобализации')

        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/columb.webp'))
        self.first_label.setText('Христофор Колумб в Америке')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/vasko.webp'))
        self.second_label.setText('Васко Да Гама в Индии')
    
    def open_next_lesson(self):
        self.first_lesson_window = NewEraFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = RevivalFirstLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = RevivalEra()
        self.back.show()
        self.hide()


class RevivalFirstLesson(Lesson):
    def __init__(self):
        super().__init__() 

        self.main_text.setHtml(REVIVAL_1_FORMATTED)
        self.heading_label.setText('Реформация')
    
    def open_next_lesson(self):
        self.next_lesson_window = RevivalSecondLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = MiddleAgesSecondLesson()
        self.previous_lesson_window.show()
        self.hide() 
    
    def return_back(self):
        self.return_window = RevivalEra()
        self.return_window.show()
        self.hide()


class MiddleAgesFirstLesson(Lesson):
    def __init__(self):
        super().__init__()
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/scheme.webp'))
        self.first_label.setText('Схема феодальной иерархии')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/knight.jpg'))
        self.fourth_label.setText('Иллюстрация рыцаря')

        self.third_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/crestiane_life.webp'))
        self.third_label.setText('Сцена из жизни крестьян')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/feodal_zamok.webp'))
        self.second_label.setText('Средневековый замок')

        self.heading_label.setText('Феодализм в Европе')

        self.main_text.setHtml(MIDDLE_AGES_1_FORMATTED)
    
    def open_next_lesson(self):
        self.next_lesson_window = MiddleAgesSecondLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = AncientThirdLesson()
        self.previous_lesson_window.show()
        self.hide() 

    def return_back(self):
        self.middle_ages_window = Middle_Ages()
        self.middle_ages_window.show()
        self.hide() 


class MiddleAgesSecondLesson(Lesson):
    def __init__(self):
        super().__init__()
        
        self.main_text.setHtml(MIDDLE_AGES_2_FORMATTED)
        self.heading_label.setText('Крестовые походы и их последствия')
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/krest_pohod.webp'))
        self.first_label.setText('Битва близ Иерусалима')
        
        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/taking_of_jerusalem.webp'))
        self.fourth_label.setText('Взятие Иерусалима')
    
    def return_back(self):
        self.ancient_times = Middle_Ages()
        self.ancient_times.show()
        self.hide()
    
    def open_next_lesson(self):
        self.next_lesson_window = RevivalFirstLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = MiddleAgesFirstLesson()
        self.previous_lesson_window.show()
        self.hide() 


class QuizResult(QMainWindow, Ui_QuizResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu_button.clicked.connect(self.open_menu)
        self.restart_button.clicked.connect(self.restart_quiz)

        self.result_label.setText(f'{CORRECT_ANSWERS} из {AMOUNT_OF_QUESTIONS} баллов')

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')  
    
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

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
           
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


class AncientThirdLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(ANCIENT_3_FORMMATED)
        self.heading_label.setText('Религиозные и философские учения')
    
    def return_back(self):
        self.ancient_times_window = Ancient_World()
        self.ancient_times_window.show()
        self.hide()
    
    def open_next_lesson(self):
        self.next_lesson_window = MiddleAgesFirstLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = AncientSecondLesson()
        self.previous_lesson_window.show()
        self.hide()

class AncientSecondLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(ANCIENT_2_FORMMATED)
        self.heading_label.setText('Античная Греция и Рим')

        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/coleseum.webp'))
        self.first_label.setText('Римский Колизей')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/parphenon.webp'))
        self.fourth_label.setText('Древнегреческий Парфенон')
    
    def return_back(self):
        self.ancient_times_window = Ancient_World()
        self.ancient_times_window.show()
        self.hide()
    
    def open_next_lesson(self):
        self.next_lesson_window = AncientThirdLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = AncientFirstLesson()
        self.previous_lesson_window.show()
        self.hide()


class AncientFirstLesson(Lesson):
    def __init__(self):
        super().__init__()

        self.main_text.setHtml(ANCIENT_1_FORMMATED)
        self.heading_label.setText('Появление цивилизаций')
    
    def open_next_lesson(self):
        self.first_lesson_window = AncientSecondLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = ModernWorldFirstLesson()
        self.previous_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Ancient_World()
        self.lessons.show()
        self.hide()


class Middle_Ages(QMainWindow, Ui_MiddleAges):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
            
    def open_first_lesson(self):
        self.first_lesson_window = MiddleAgesFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = MiddleAgesSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
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

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
    def open_first_lesson(self):
        self.first_lesson_window = AncientFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = AncientSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def open_third_lesson(self):
        self.third_lesson_window = AncientThirdLesson()
        self.third_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class RevivalEra(QMainWindow, Ui_RevivalEra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.second_lesson.clicked.connect(self.open_first_lesson)
        self.third_lesson.clicked.connect(self.open_second_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
    def open_first_lesson(self):
        self.first_lesson_window = RevivalFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = RevivalSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class NewEra(QMainWindow, Ui_NewEra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
    def open_first_lesson(self):
        self.first_lesson_window = NewEraFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
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
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
        
    def open_first_lesson(self):
        self.first_lesson_window = TwentyCenturyFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = TwentyCenturySecondLesson()
        self.second_lesson_window.show()
        self.hide()

    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class ModernWorld(QMainWindow, Ui_ModernWorld):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.third_lesson.clicked.connect(self.open_first_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

    def open_first_lesson(self):
        self.first_lesson_window = ModernWorldFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
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

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
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

        if THEME == 'dark':
            change_on_dark_theme(self)
            
            self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: #151719;
            }
            QCalendarWidget QAbstractItemView {
                color: white;
            }            
            QHeaderView::section {
                background-color: #151719;
                color: white;
                font-weight: bold;
            QComboBox {
                background-color: #151719;
                color: white;
            }
            }
        """)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
            self.calendar.setStyleSheet(""" QCalendarWidget QAbstractItemView {
                color: black; """)
        
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

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
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
        
        self.back_button.setIcon(QIcon('data/icons/return.svg'))

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
            
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


class Settings(QMainWindow, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save_changes_button.clicked.connect(self.update_changes)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
            
    def update_changes(self):
        global THEME

        if self.theme_choose.currentText() == 'Темная':
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Подтверждение изменений')
            msg_box.setText('Вы хотите применить изменения?')

            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            msg_box.button(QMessageBox.StandardButton.Yes).setText('Да')
            msg_box.button(QMessageBox.StandardButton.No).setText('Нет')

            result = msg_box.exec()

            if result == QMessageBox.StandardButton.Yes:
                THEME = 'dark'
                self.setStyleSheet('background-color: #151719;')
                self.theme_choose.setCurrentIndex(1)

                for widget in self.widgets:
                    widget.setStyleSheet('color: white;')
            else:
                ...
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Подтверждение изменений')
            msg_box.setText('Вы хотите применить изменения?')

            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            msg_box.button(QMessageBox.StandardButton.Yes).setText('Да')
            msg_box.button(QMessageBox.StandardButton.No).setText('Нет')

            result = msg_box.exec()

            if result == QMessageBox.StandardButton.Yes:
                self.theme_choose.setCurrentIndex(0)
                self.setStyleSheet('background-color: #ffe4b5;')
                THEME = 'light'
                
                for widget in self.widgets:
                    widget.setStyleSheet('color: black;')
            
            else:
                ...

    def return_back(self):
        self.menu_window = MainMenu()
        self.menu_window.show()
        self.hide()


class Help(QMainWindow, Ui_Help):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
    
    def return_back(self):
        self.back = MainMenu()
        self.back.show()
        self.hide()


class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.quiz_button.setIcon(QIcon('data/icons/quiz.svg'))
        self.help_button.setIcon(QIcon('data/icons/help.svg'))
        self.settings_button.setIcon(QIcon('data/icons/settings.svg'))
        self.book_button.setIcon(QIcon('data/icons/book.svg'))
        
        self.help_button.clicked.connect(self.open_help)
        self.book_button.clicked.connect(self.open_book)
        self.quiz_button.clicked.connect(self.open_quiz)
        self.settings_button.clicked.connect(self.open_settings)

        if THEME == 'dark':
            change_on_dark_theme(self)
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

            
    def open_quiz(self):
        self.quiz_introduction = QuizInroduction()
        self.quiz_introduction.show()
        self.hide()

    def open_book(self):
        self.book = Book()
        self.book.show()
        self.hide()
    
    def open_settings(self):
        self.settings_window = Settings()
        self.settings_window.show()
        self.hide()
    
    def open_help(self):
        self.help_window = Help()
        self.help_window.show()
        self.hide()