from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon

class Ui_ModernWorld(object):
    def setupUi(self, ModernWorld):
        ModernWorld.setObjectName("ModernWorld")
        ModernWorld.resize(949, 759)
        self.centralwidget = QtWidgets.QWidget(parent=ModernWorld)
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
        self.modern_world = QtWidgets.QLabel(parent=self.centralwidget)
        self.modern_world.setGeometry(QtCore.QRect(10, 0, 941, 71))
        self.modern_world.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.modern_world.setObjectName("modern_world")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(400, 460, 161, 28))
        self.return_button.setObjectName("return_button")
        ModernWorld.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ModernWorld)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 26))
        self.menubar.setObjectName("menubar")
        ModernWorld.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ModernWorld)
        self.statusbar.setObjectName("statusbar")
        ModernWorld.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 12)
        self.average_font = QFont('Rockwell Extra Bold', 8)
        self.small_font = QFont('Rockwell Extra Bold', 7)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.modern_world.setFont(self.big_font)
        self.first_lesson.setFont(self.average_font)
        self.second_lesson.setFont(self.average_font)
        self.third_lesson.setFont(self.average_font)
        self.return_button.setFont(self.small_font)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.widgets = [self.first_lesson, self.second_lesson, self.third_lesson,
                        self.modern_world, self.return_button]

        self.retranslateUi(ModernWorld)
        QtCore.QMetaObject.connectSlotsByName(ModernWorld)

    def retranslateUi(self, ModernWorld):
        _translate = QtCore.QCoreApplication.translate
        ModernWorld.setWindowTitle(_translate("ModernWorld", "ModernWorld"))
        self.first_lesson.setText(_translate("ModernWorld", "Урок 1. Глобализация и её последствия"))
        self.second_lesson.setText(_translate("ModernWorld", "Урок 2. Конфликты и кризисы XXI века"))
        self.third_lesson.setText(_translate("ModernWorld", "Урок 3. Развитие технологий и их влияние на общество"))
        self.modern_world.setText(_translate("ModernWorld", "Современный мир"))
        self.return_button.setText(_translate("ModernWorld", "Вернуться назад"))