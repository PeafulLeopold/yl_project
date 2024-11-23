from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon

class Ui_MiddleAges(object):
    def setupUi(self, MiddleAges):
        MiddleAges.setObjectName("MiddleAges")
        MiddleAges.resize(949, 759)
        self.centralwidget = QtWidgets.QWidget(parent=MiddleAges)
        self.centralwidget.setObjectName("centralwidget")
        self.first_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.first_lesson.setGeometry(QtCore.QRect(220, 180, 521, 61))
        self.first_lesson.setObjectName("first_lesson")
        self.second_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.second_lesson.setGeometry(QtCore.QRect(220, 250, 521, 61))
        self.second_lesson.setObjectName("second_lesson")
        self.ancient_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ancient_label.setGeometry(QtCore.QRect(10, 0, 941, 71))
        self.ancient_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ancient_label.setObjectName("ancient_label")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(400, 460, 161, 28))
        self.return_button.setObjectName("return_button")
        MiddleAges.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MiddleAges)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 26))
        self.menubar.setObjectName("menubar")
        MiddleAges.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MiddleAges)
        self.statusbar.setObjectName("statusbar")
        MiddleAges.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 12)
        self.average_font = QFont('Rockwell Extra Bold', 8)
        self.small_font = QFont('Rockwell Extra Bold', 7)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.ancient_label.setFont(self.big_font)
        self.first_lesson.setFont(self.average_font)
        self.second_lesson.setFont(self.average_font)
        self.return_button.setFont(self.small_font)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.widgets = [self.first_lesson, self.second_lesson,
                        self.ancient_label, self.return_button]

        self.retranslateUi(MiddleAges)
        QtCore.QMetaObject.connectSlotsByName(MiddleAges)

    def retranslateUi(self, MiddleAges):
        _translate = QtCore.QCoreApplication.translate
        MiddleAges.setWindowTitle(_translate("MiddleAges", "MiddleAges"))
        self.first_lesson.setText(_translate("MiddleAges", "Урок 1. Феодализм в Европе"))
        self.second_lesson.setText(_translate("MiddleAges", "Урок 2. Крестовые походы и их последствия"))
        self.ancient_label.setText(_translate("MiddleAges", "Средневековье"))
        self.return_button.setText(_translate("MiddleAges", "Вернуться назад"))
