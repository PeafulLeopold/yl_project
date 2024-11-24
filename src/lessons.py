from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from py_items.design_lessons import Ui_Lessons
from revival_era import RevivalEra
from ancient_world import Ancient_World
from new_era import NewEra
from modern_world import ModernWorld
from twenty_century import TwentyCentury
from middle_ages import Middle_Ages
from book import Book

class Lessons(QMainWindow, Ui_Lessons):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.return_button.clicked.connect(self.return_back)
        self.lessons_button.clicked.connect(self.open_lesson)
        self.setStyleSheet('background-color: #ffe4b5')
    
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