from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(909, 738)
        self.centralwidget = QtWidgets.QWidget(parent=Help)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(0, 0, 911, 81))
        self.heading_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        self.answers_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.answers_label.setGeometry(QtCore.QRect(30, 125, 841, 51))
        self.answers_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.answers_label.setObjectName("answers_label")
        self.first_question_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.first_question_label.setGeometry(QtCore.QRect(10, 202, 901, 51))
        self.first_question_label.setObjectName("first_question_label")
        self.first_answer_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.first_answer_label.setGeometry(QtCore.QRect(10, 250, 901, 51))
        self.first_answer_label.setObjectName("first_answer_label")
        self.second_question_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.second_question_label.setGeometry(QtCore.QRect(10, 322, 901, 51))
        self.second_question_label.setObjectName("second_question_label")
        self.second_answer_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.second_answer_label.setGeometry(QtCore.QRect(10, 370, 901, 51))
        self.second_answer_label.setObjectName("second_answer_label")
        self.addition_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.addition_label.setGeometry(QtCore.QRect(10, 410, 901, 51))
        self.addition_label.setObjectName("addition_label")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(360, 580, 171, 41))
        self.return_button.setObjectName("return_button")
        Help.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Help)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 26))
        self.menubar.setObjectName("menubar")
        Help.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Help)
        self.statusbar.setObjectName("statusbar")
        Help.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 16)
        self.under_big_font = QFont('Rockwell Extra Bold', 12)
        self.small_font = QFont('Rockwell Extra Bold', 9)
        self.avg_font = QFont('Rockwell Extra Bold', 11)

        self.big_font.setBold(True)
        self.under_big_font.setBold(True)
        self.small_font.setBold(True)
        self.avg_font.setBold(True)

        self.heading_label.setFont(self.big_font)
        self.answers_label.setFont(self.under_big_font)
        self.first_question_label.setFont(self.avg_font)
        self.first_answer_label.setFont(self.small_font)
        self.second_question_label.setFont(self.avg_font)
        self.second_answer_label.setFont(self.small_font)
        self.return_button.setFont(self.small_font)
        self.addition_label.setFont(self.small_font)

        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.widgets = [self.heading_label, self.answers_label, self.first_question_label,
                        self.first_answer_label, self.second_question_label,
                        self.second_answer_label, self.return_button, self.addition_label]

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Help"))
        self.heading_label.setText(_translate("Help", "Добро пожаловать в раздел \'\'Помощь\'\'"))
        self.answers_label.setText(_translate("Help", "Ответы на частозадаваемые вопросы"))
        self.first_question_label.setText(_translate("Help", "1. Как начать обучение?"))
        self.first_answer_label.setText(_translate("Help", "Ответ: Для того, чтобы начать обучение перейдите в  \'\'Учебник\'\'->\'\'Уроки\'\' и выберите интересующую эпоху"))
        self.second_question_label.setText(_translate("Help", "2. Как взаимодействовать с интерактивным календарем?"))
        self.second_answer_label.setText(_translate("Help", "Ответ: Чтобы получить информацию о дате, вам нужно нажать на интересующую вас дату на самом календаре"))
        self.addition_label.setText(_translate("Help", "Помечание: в календаре присутствует информация только о значимых датах"))
        self.return_button.setText(_translate("Help", "Назад"))
