from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QVBoxLayout


class Ui_MainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainMenu")
        MainWindow.resize(1170, 1300)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.quiz_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.quiz_button.setGeometry(QtCore.QRect(380, 270, 371, 91))
        self.quiz_button.setObjectName("quiz_button")
        self.book_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.book_button.setGeometry(QtCore.QRect(380, 360, 371, 91))
        self.book_button.setObjectName("book_button")
        self.section_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.section_label.setGeometry(QtCore.QRect(460, 170, 211, 71))
        self.section_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.section_label.setObjectName("section_label")
        self.help_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(430, 480, 261, 61))
        self.help_button.setObjectName("help_button")
        self.settings_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(430, 540, 261, 61))
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.settings_button.setObjectName("settings_button")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 0, 731, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_label = QtWidgets.QLabel(parent=self.widget)
        self.welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout.addWidget(self.welcome_label)
        self.target_label = QtWidgets.QLabel(parent=self.widget)
        self.target_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.target_label.setObjectName("target_label")
        self.verticalLayout.addWidget(self.target_label)
        MainWindow.setCentralWidget(self.centralwidget)
        
        welcome_font = QFont('Rockwell Extra Bold', 14)
        font_big = QFont('Rockwell Extra Bold', 9)
        font_small = QFont('Rockwell Extra Bold', 8)
        font_big.setBold(True)
        font_small.setBold(True)
        welcome_font.setBold(True)

        self.quiz_button.setFont(font_big)
        self.help_button.setFont(font_small)
        self.settings_button.setFont(font_small)
        self.book_button.setFont(font_big)
        self.target_label.setFont(font_small)
        self.section_label.setFont(welcome_font)
        self.welcome_label.setFont(welcome_font)

        self.widgets = [self.quiz_button, self.help_button, self.settings_button,
                        self.book_button, self.section_label,
                        self.welcome_label, self.target_label]
        
        self.target_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.section_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainMenu"))
        self.quiz_button.setText(_translate("MainWindow", "Викторина"))
        self.book_button.setText(_translate("MainWindow", "Учебник"))
        self.section_label.setText(_translate("MainWindow", "Выберите раздел"))
        self.help_button.setText(_translate("MainWindow", "Помощь"))
        self.settings_button.setText(_translate("MainWindow", "Настройки"))
        self.welcome_label.setText(_translate("MainWindow", "Добро пожаловать в приложение StudyHistory! "))
        self.target_label.setText(_translate("MainWindow", "Цель этого приложения - усовершенствовать познания пользователей в области мировой истории"))
