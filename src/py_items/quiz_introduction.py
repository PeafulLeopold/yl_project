from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon


class Ui_QuizIntroduction(object):
    def setupUi(self, QuizIntroduction):
        QuizIntroduction.setObjectName("QuizIntroduction")
        QuizIntroduction.resize(845, 748)
        self.centralwidget = QtWidgets.QWidget(parent=QuizIntroduction)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(0, 0, 831, 91))
        self.heading_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        self.level_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.level_label.setGeometry(QtCore.QRect(140, 180, 311, 61))
        self.level_label.setObjectName("level_label")
        self.chosen_level = QtWidgets.QComboBox(parent=self.centralwidget)
        self.chosen_level.setGeometry(QtCore.QRect(530, 190, 161, 41))
        self.chosen_level.setObjectName("chosen_level")
        self.chosen_level.addItem("")
        self.chosen_level.addItem("")
        self.chosen_level.addItem("")
        self.questions_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.questions_label.setGeometry(QtCore.QRect(140, 300, 311, 61))
        self.questions_label.setObjectName("questions_label")
        self.amount_of_questions = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.amount_of_questions.setGeometry(QtCore.QRect(530, 310, 161, 41))
        self.amount_of_questions.setObjectName("amount_of_questions")
        self.next_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(310, 460, 200, 31))
        self.next_button.setObjectName("next_button")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(310, 500, 200, 31))
        self.return_button.setObjectName("return_button")
        QuizIntroduction.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=QuizIntroduction)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 23))
        self.menubar.setObjectName("menubar")
        QuizIntroduction.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=QuizIntroduction)
        self.statusbar.setObjectName("statusbar")
        QuizIntroduction.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 12)
        self.under_big_font = QFont('Rockwell Extra Bold', 9)
        self.average_font = QFont('Rockwell Extra Bold', 8)

        self.big_font.setBold(True)
        self.under_big_font.setBold(True)
        self.average_font.setBold(True)

        self.heading_label.setFont(self.big_font)
        self.level_label.setFont(self.under_big_font)
        self.questions_label.setFont(self.under_big_font)
        self.chosen_level.setFont(self.average_font)
        self.return_button.setFont(self.average_font)
        self.next_button.setFont(self.average_font)
        self.amount_of_questions.setFont(self.under_big_font)

        self.widgets = [self.heading_label, self.level_label, self.questions_label,
                        self.chosen_level, self.return_button, self.next_button,
                        self.amount_of_questions]

        self.amount_of_questions.setMaximum(15)
        self.amount_of_questions.setMinimum(1)
        
        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.retranslateUi(QuizIntroduction)
        QtCore.QMetaObject.connectSlotsByName(QuizIntroduction)

    def retranslateUi(self, QuizIntroduction):
        _translate = QtCore.QCoreApplication.translate
        QuizIntroduction.setWindowTitle(_translate("QuizIntroduction", "QuizIntroduction"))
        self.heading_label.setText(_translate("QuizIntroduction", "Перед началом викторины:"))
        self.level_label.setText(_translate("QuizIntroduction", " 1. Укажите уровень "))
        self.chosen_level.setItemText(0, _translate("QuizIntroduction", "Новичок"))
        self.chosen_level.setItemText(1, _translate("QuizIntroduction", "Любитель"))
        self.chosen_level.setItemText(2, _translate("QuizIntroduction", "Эксперт"))
        self.questions_label.setText(_translate("QuizIntroduction", " 2. Укажите количество вопросов"))
        self.next_button.setText(_translate("QuizIntroduction", "Начать!"))
        self.return_button.setText(_translate("QuizIntroduction", "Назад"))
