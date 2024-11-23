from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon

class Ui_RevivalEra(object):
    def setupUi(self, RevivalEra):
        RevivalEra.setObjectName("RevivalEra")
        RevivalEra.resize(949, 759)
        self.centralwidget = QtWidgets.QWidget(parent=RevivalEra)
        self.centralwidget.setObjectName("centralwidget")
        self.first_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.second_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.second_lesson.setGeometry(QtCore.QRect(220, 180, 521, 61))
        self.second_lesson.setObjectName("second_lesson")
        self.third_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.third_lesson.setGeometry(QtCore.QRect(220, 250, 521, 61))
        self.third_lesson.setObjectName("third_lesson")
        self.ancient_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ancient_label.setGeometry(QtCore.QRect(10, 0, 941, 71))
        self.ancient_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ancient_label.setObjectName("ancient_label")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(400, 460, 161, 28))
        self.return_button.setObjectName("return_button")
        RevivalEra.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RevivalEra)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 26))
        self.menubar.setObjectName("menubar")
        RevivalEra.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RevivalEra)
        self.statusbar.setObjectName("statusbar")
        RevivalEra.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 12)
        self.average_font = QFont('Rockwell Extra Bold', 8)
        self.small_font = QFont('Rockwell Extra Bold', 7)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.ancient_label.setFont(self.big_font)
        self.second_lesson.setFont(self.average_font)
        self.third_lesson.setFont(self.average_font)
        self.return_button.setFont(self.small_font)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.widgets = [self.second_lesson, self.third_lesson,
                        self.ancient_label, self.return_button]

        self.retranslateUi(RevivalEra)
        QtCore.QMetaObject.connectSlotsByName(RevivalEra)

    def retranslateUi(self, RevivalEra):
        _translate = QtCore.QCoreApplication.translate
        RevivalEra.setWindowTitle(_translate("RevivalEra", "RevivalEra"))
        self.second_lesson.setText(_translate("RevivalEra", "Урок 1. Реформация и её влияние на религию и общество"))
        self.third_lesson.setText(_translate("RevivalEra", "Урок 2. Начало колонизации и глобализации"))
        self.ancient_label.setText(_translate("RevivalEra", "Эра Возрождения и Реформации"))
        self.return_button.setText(_translate("RevivalEra", "Вернуться назад"))