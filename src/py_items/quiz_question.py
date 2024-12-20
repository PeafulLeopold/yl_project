from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont


class Ui_QuizQuestion(object):
    def setupUi(self, QuizQuestion):
        QuizQuestion.setObjectName("QuizQuestion")
        QuizQuestion.resize(956, 718)
        self.centralwidget = QtWidgets.QWidget(parent=QuizQuestion)
        self.centralwidget.setObjectName("centralwidget")
        self.question_number_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.question_number_label.setGeometry(QtCore.QRect(0, 0, 961, 81))
        self.question_number_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.question_number_label.setObjectName("question_number_label")
        self.question_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.question_label.setGeometry(QtCore.QRect(0, 100, 951, 151))
        self.question_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.question_label.setObjectName("question_label")
        self.first_variant_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.first_variant_button.setGeometry(QtCore.QRect(30, 320, 431, 81))
        self.first_variant_button.setObjectName("first_variant_button")
        self.third_variant_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.third_variant_button.setGeometry(QtCore.QRect(490, 320, 431, 81))
        self.third_variant_button.setObjectName("third_variant_button")
        self.fourth_variant_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fourth_variant_button.setGeometry(QtCore.QRect(490, 450, 431, 81))
        self.fourth_variant_button.setObjectName("fourth_variant_button")
        self.second_variant_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.second_variant_button.setGeometry(QtCore.QRect(30, 450, 431, 81))
        self.second_variant_button.setObjectName("second_variant_button")
        self.next_question_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_question_button.setGeometry(QtCore.QRect(480, 590, 181, 51))
        self.next_question_button.setObjectName("next_question_button")
        self.end_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.end_button.setGeometry(QtCore.QRect(280, 590, 191, 51))
        self.end_button.setObjectName("end_button")
        QuizQuestion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=QuizQuestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 26))
        self.menubar.setObjectName("menubar")
        QuizQuestion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=QuizQuestion)
        self.statusbar.setObjectName("statusbar")
        QuizQuestion.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 14)
        self.average_font = QFont('Rockwell Extra Bold', 12)
        self.small_font = QFont('Rockwell Extra Bold', 8)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.question_label.setFont(self.average_font)
        self.question_number_label.setFont(self.big_font)
        self.first_variant_button.setFont(self.small_font)
        self.second_variant_button.setFont(self.small_font)
        self.third_variant_button.setFont(self.small_font)
        self.fourth_variant_button.setFont(self.small_font)
        self.end_button.setFont(self.small_font)
        self.next_question_button.setFont(self.small_font)

        self.widgets = [self.question_label, self.question_number_label, self.first_variant_button,
                        self.second_variant_button, self.third_variant_button, self.fourth_variant_button,
                        self.end_button, self.next_question_button]

        self.retranslateUi(QuizQuestion)
        QtCore.QMetaObject.connectSlotsByName(QuizQuestion)

    def retranslateUi(self, QuizQuestion):
        _translate = QtCore.QCoreApplication.translate
        QuizQuestion.setWindowTitle(_translate("QuizQuestion", "QuizQuestion"))
        self.question_number_label.setText(_translate("QuizQuestion", "Вопрос №"))
        self.question_label.setText(_translate("QuizQuestion", "Вопрос"))
        self.first_variant_button.setText(_translate("QuizQuestion", "Вариант ответа №1"))
        self.third_variant_button.setText(_translate("QuizQuestion", "Вариант ответа №3"))
        self.fourth_variant_button.setText(_translate("QuizQuestion", "Вариант ответа №4"))
        self.second_variant_button.setText(_translate("QuizQuestion", "Вариант ответа №2"))
        self.next_question_button.setText(_translate("QuizQuestion", "Следующий вопрос"))
        self.end_button.setText(_translate("QuizQuestion", "Закончить"))
