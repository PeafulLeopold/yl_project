from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon


class Ui_QuizResult(object):
    def setupUi(self, QuizResult):
        QuizResult.setObjectName("QuizResult")
        QuizResult.resize(850, 643)
        self.centralwidget = QtWidgets.QWidget(parent=QuizResult)
        self.centralwidget.setObjectName("centralwidget")
        self.congratulations_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.congratulations_label.setGeometry(QtCore.QRect(-4, 0, 851, 71))
        self.congratulations_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.congratulations_label.setObjectName("congratulations_label")
        self.summing_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.summing_label.setGeometry(QtCore.QRect(0, 80, 851, 71))
        self.summing_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.summing_label.setObjectName("summing_label")
        self.result_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(0, 200, 851, 71))
        self.result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.restart_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(220, 410, 161, 61))
        self.restart_button.setObjectName("restart_button")
        self.menu_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.menu_button.setGeometry(QtCore.QRect(460, 410, 161, 61))
        self.menu_button.setObjectName("menu_button")
        QuizResult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=QuizResult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        QuizResult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=QuizResult)
        self.statusbar.setObjectName("statusbar")
        QuizResult.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 16)
        self.under_big_font = QFont('Rockwell Extra Bold', 14)
        self.average_font = QFont('Rockwell Extra Bold', 12)
        self.small_font = QFont('Rockwell Extra Bold', 8)

        self.big_font.setBold(True)
        self.under_big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.congratulations_label.setFont(self.big_font)
        self.summing_label.setFont(self.average_font)
        self.result_label.setFont(self.under_big_font)
        self.restart_button.setFont(self.small_font)
        self.menu_button.setFont(self.small_font)

        self.widgets = [self.congratulations_label, self.summing_label, self.result_label,
                        self.restart_button, self.menu_button]

        self.menu_button.setIcon(QIcon('data/icons/menu.svg'))
        self.restart_button.setIcon(QIcon('data/icons/restart.svg'))

        self.retranslateUi(QuizResult)
        QtCore.QMetaObject.connectSlotsByName(QuizResult)

    def retranslateUi(self, QuizResult):
        _translate = QtCore.QCoreApplication.translate
        QuizResult.setWindowTitle(_translate("QuizResult", "QuizResult"))
        self.congratulations_label.setText(_translate("QuizResult", "Поздравляю! "))
        self.summing_label.setText(_translate("QuizResult", "Вы прошли викторину, набрав:"))
        self.result_label.setText(_translate("QuizResult", "5 из 6 баллов"))
        self.restart_button.setText(_translate("QuizResult", "Начать заново"))
        self.menu_button.setText(_translate("QuizResult", "Главное меню"))
