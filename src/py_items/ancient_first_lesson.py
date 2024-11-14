from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QPixmap, QFont

class Ui_AncientFirstLesson(object):
    def setupUi(self, AncientFirstLesson):
        AncientFirstLesson.setObjectName("AncientFirstLesson")
        AncientFirstLesson.resize(937, 684)
        self.centralwidget = QtWidgets.QWidget(parent=AncientFirstLesson)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(-10, 0, 951, 61))
        self.heading_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        self.first_paragraph = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.first_paragraph.setGeometry(QtCore.QRect(460, 90, 301, 241))
        self.first_paragraph.setObjectName("first_paragraph")
        self.second_paragraph = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.second_paragraph.setGeometry(QtCore.QRect(160, 330, 301, 241))
        self.second_paragraph.setObjectName("second_paragraph")
        self.first_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.first_photo.setGeometry(QtCore.QRect(150, 90, 291, 221))
        self.first_photo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.first_photo.setObjectName("first_photo")
        self.second_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.second_photo.setGeometry(QtCore.QRect(480, 340, 291, 221))
        self.second_photo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.second_photo.setObjectName("second_photo")
        self.next_lesson_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_lesson_button.setGeometry(QtCore.QRect(820, 260, 111, 81))
        self.next_lesson_button.setObjectName("next_lesson_button")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(390, 600, 151, 28))
        self.return_button.setObjectName("return_button")
        AncientFirstLesson.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AncientFirstLesson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 26))
        self.menubar.setObjectName("menubar")
        AncientFirstLesson.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AncientFirstLesson)
        self.statusbar.setObjectName("statusbar")
        AncientFirstLesson.setStatusBar(self.statusbar)

        small_font = QFont('Rockwell Extra Bold', 7)
        big_font = QFont('Rockwell Extra Bold', 12)
        small_font.setBold(True)
        big_font.setBold(True)

        self.heading_label.setFont(big_font)
        self.return_button.setFont(small_font)
        self.next_lesson_button.setFont(small_font)

        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.next_lesson_button.setIcon(QIcon('data/icons/next.svg'))

        self.first_photo.setPixmap(QPixmap('data/lessons_photo/civ1.webp'))
        self.second_photo.setPixmap(QPixmap('data/lessons_photo/civ2.webp'))

        self.first_photo.setScaledContents(True)
        self.second_photo.setScaledContents(True)

        self.retranslateUi(AncientFirstLesson)
        QtCore.QMetaObject.connectSlotsByName(AncientFirstLesson)

    def retranslateUi(self, AncientFirstLesson):
        _translate = QtCore.QCoreApplication.translate
        AncientFirstLesson.setWindowTitle(_translate("AncientFirstLesson", "AncientFirstLesson"))
        self.heading_label.setText(_translate("AncientFirstLesson", "Урок 1. Появление цивилизаций"))
        self.first_photo.setText(_translate("AncientFirstLesson", ""))
        self.second_photo.setText(_translate("AncientFirstLesson", ""))
        self.next_lesson_button.setText(_translate("AncientFirstLesson", "Следующий урок"))
        self.return_button.setText(_translate("AncientFirstLesson", "Вернуться назад"))
