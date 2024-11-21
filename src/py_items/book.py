from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont


class Ui_Book(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 790)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.book_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.book_label.setGeometry(QtCore.QRect(230, 30, 501, 41))
        self.book_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.book_label.setObjectName("book_label")
        self.calendar_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calendar_button.setGeometry(QtCore.QRect(80, 230, 231, 81))
        self.calendar_button.setObjectName("calendar_button")
        self.lesson_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.lesson_button.setGeometry(QtCore.QRect(370, 230, 231, 81))
        self.lesson_button.setObjectName("lesson_button")
        self.sources_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sources_button.setGeometry(QtCore.QRect(670, 230, 231, 81))
        self.sources_button.setObjectName("sources_button")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(370, 460, 231, 28))
        self.back_button.setObjectName("back_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 12)
        self.average_font = QFont('Rockwell Extra Bold', 8)
        self.small_font = QFont('Rockwell Extra Bold', 7)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.book_label.setFont(self.big_font)
        self.calendar_button.setFont(self.average_font)
        self.lesson_button.setFont(self.average_font)
        self.sources_button.setFont(self.average_font)        
        self.back_button.setFont(self.small_font)

        self.widgets = [self.book_label, self.calendar_button,
                        self.lesson_button, self.sources_button,
                        self.back_button]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.book_label.setText(_translate("MainWindow", "Учебник"))
        self.calendar_button.setText(_translate("MainWindow", "Календарь событий"))
        self.lesson_button.setText(_translate("MainWindow", "Уроки"))
        self.sources_button.setText(_translate("MainWindow", "Полезные материалы"))
        self.back_button.setText(_translate("MainWindow", "Вернуться назад"))
