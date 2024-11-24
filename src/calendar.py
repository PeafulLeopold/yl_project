from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon, QTextCharFormat, QColor
from PyQt6 import QtCore

from py_items.design_calendar import Ui_Calendar
from py_items.config import EVENTS
from book import Book


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
