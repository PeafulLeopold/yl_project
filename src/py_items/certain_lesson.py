from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon

class Ui_CertainLesson(object):
    def setupUi(self, CertainLesson):
        CertainLesson.setObjectName("CertainLesson")
        CertainLesson.resize(949, 759)
        self.centralwidget = QtWidgets.QWidget(parent=CertainLesson)
        self.centralwidget.setObjectName("centralwidget")
        self.first_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.first_lesson.setGeometry(QtCore.QRect(220, 180, 521, 61))
        self.first_lesson.setObjectName("first_lesson")
        self.second_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.second_lesson.setGeometry(QtCore.QRect(220, 250, 521, 61))
        self.second_lesson.setObjectName("second_lesson")
        self.third_lesson = QtWidgets.QPushButton(parent=self.centralwidget)
        self.third_lesson.setGeometry(QtCore.QRect(220, 320, 521, 61))
        self.third_lesson.setObjectName("third_lesson")
        self.name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(10, 0, 941, 71))
        self.name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(400, 460, 161, 28))
        self.return_button.setObjectName("return_button")
        CertainLesson.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=CertainLesson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 26))
        self.menubar.setObjectName("menubar")
        CertainLesson.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=CertainLesson)
        self.statusbar.setObjectName("statusbar")
        CertainLesson.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 12)
        self.average_font = QFont('Rockwell Extra Bold', 8)
        self.small_font = QFont('Rockwell Extra Bold', 7)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.name_label.setFont(self.big_font)
        self.first_lesson.setFont(self.average_font)
        self.second_lesson.setFont(self.average_font)
        self.third_lesson.setFont(self.average_font)
        self.return_button.setFont(self.small_font)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.retranslateUi(CertainLesson)
        QtCore.QMetaObject.connectSlotsByName(CertainLesson)

    def retranslateUi(self, CertainLesson):
        _translate = QtCore.QCoreApplication.translate
        CertainLesson.setWindowTitle(_translate("CertainLesson", "CertainLesson"))
        self.first_lesson.setText(_translate("CertainLesson", ""))
        self.second_lesson.setText(_translate("CertainLesson", ""))
        self.third_lesson.setText(_translate("CertainLesson", ""))
        self.name_label.setText(_translate("CertainLesson", ""))
        self.return_button.setText(_translate("CertainLesson", ""))