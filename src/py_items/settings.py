from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QIcon

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(837, 636)
        self.centralwidget = QtWidgets.QWidget(parent=Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(0, 0, 831, 61))
        self.heading_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        self.theme_choose = QtWidgets.QComboBox(parent=self.centralwidget)
        self.theme_choose.setGeometry(QtCore.QRect(290, 170, 350, 41))
        self.theme_choose.setObjectName("theme_choose")
        self.theme_choose.addItem("")
        self.theme_choose.addItem("")
        self.theme_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.theme_label.setGeometry(QtCore.QRect(40, 170, 161, 41))
        self.theme_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.theme_label.setObjectName("theme_label")
        self.save_changes_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_changes_button.setGeometry(QtCore.QRect(330, 450, 181, 51))
        self.save_changes_button.setObjectName("save_changes_button")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(330, 510, 181, 51))
        self.return_button.setObjectName("return_button")
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 23))
        self.menubar.setObjectName("menubar")
        Settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Settings)
        self.statusbar.setObjectName("statusbar")
        Settings.setStatusBar(self.statusbar)

        self.big_font = QFont('Rockwell Extra Bold', 16)
        self.average_font = QFont('Rockwell Extra Bold', 9)
        self.small_font = QFont('Rockwell Extra Bold', 8)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.heading_label.setFont(self.big_font)
        self.theme_choose.setFont(self.average_font)
        self.theme_label.setFont(self.average_font)
        self.save_changes_button.setFont(self.small_font)
        self.return_button.setFont(self.small_font)

        self.widgets = [self.heading_label, self.theme_choose, self.theme_label, self.save_changes_button,
                        self.return_button]

        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.heading_label.setText(_translate("Settings", "Настройки"))
        self.theme_choose.setItemText(0, _translate("Settings", "Светлая"))
        self.theme_choose.setItemText(1, _translate("Settings", "Темная"))
        self.theme_label.setText(_translate("Settings", "Тема:"))
        self.save_changes_button.setText(_translate("Settings", "Сохранить изменения"))
        self.return_button.setText(_translate("Settings", "Назад"))
