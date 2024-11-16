from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QFont, QIcon, QPixmap

class Ui_AncientFirstLesson(object):
    def setupUi(self, AncientFirstLesson):
        AncientFirstLesson.setObjectName("AncientFirstLesson")
        AncientFirstLesson.resize(1007, 746)
        self.centralwidget = QtWidgets.QWidget(parent=AncientFirstLesson)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(0, 0, 891, 61))
        self.heading_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setObjectName("label")
        self.shumer = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.shumer.setGeometry(QtCore.QRect(380, 160, 421, 101))
        self.shumer.setObjectName("shumer")
        self.ancient_china = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.ancient_china.setGeometry(QtCore.QRect(380, 320, 421, 111))
        self.ancient_china.setObjectName("ancient_china")
        self.first_civ_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.first_civ_label.setGeometry(QtCore.QRect(-60, 70, 1001, 20))
        self.first_civ_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.first_civ_label.setObjectName("first_civ_label")
        self.shumer_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.shumer_photo.setGeometry(QtCore.QRect(120, 160, 161, 101))
        self.shumer_photo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.shumer_photo.setObjectName("shumer_photo")
        self.china_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.china_photo.setGeometry(QtCore.QRect(120, 320, 161, 111))
        self.china_photo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.china_photo.setObjectName("china_photo")
        self.olmeki = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.olmeki.setGeometry(QtCore.QRect(380, 490, 421, 111))
        self.olmeki.setObjectName("olmeki")
        self.olmeki_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.olmeki_photo.setGeometry(QtCore.QRect(120, 490, 161, 111))
        self.olmeki_photo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.olmeki_photo.setObjectName("olmeki_photo")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(370, 640, 151, 28))
        self.return_button.setObjectName("return_button")
        self.next_lesson_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_lesson_button.setGeometry(QtCore.QRect(830, 330, 121, 81))
        self.next_lesson_button.setObjectName("next_lesson_button")
        AncientFirstLesson.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AncientFirstLesson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 26))
        self.menubar.setObjectName("menubar")
        AncientFirstLesson.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AncientFirstLesson)
        self.statusbar.setObjectName("statusbar")
        AncientFirstLesson.setStatusBar(self.statusbar)
        
        self.big_font = QFont('Rockwell Extra Bold', 12)
        self.average_font = QFont('Rockwell Extra Bold', 8)
        self.small_font = QFont('Rockwell Extra Bold', 7)

        self.big_font.setBold(True)
        self.average_font.setBold(True)
        self.small_font.setBold(True)

        self.heading_label.setFont(self.big_font)
        self.first_civ_label.setFont(self.average_font)
        self.next_lesson_button.setFont(self.small_font)
        self.return_button.setFont(self.small_font)

        self.next_lesson_button.setIcon(QIcon('data/icons/next.svg'))
        self.return_button.setIcon(QIcon('data/icons/return.svg'))

        self.shumer_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/shumer.png'))
        self.olmeki_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/olmeki.webp'))
        self.china_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/anc_china.webp'))
        
        self.shumer_photo.setScaledContents(True)
        self.olmeki_photo.setScaledContents(True)
        self.china_photo.setScaledContents(True)

        self.retranslateUi(AncientFirstLesson)
        QtCore.QMetaObject.connectSlotsByName(AncientFirstLesson)

    def retranslateUi(self, AncientFirstLesson):
        _translate = QtCore.QCoreApplication.translate
        AncientFirstLesson.setWindowTitle(_translate("AncientFirstLesson", "AncientFirstLesson"))
        self.heading_label.setText(_translate("AncientFirstLesson", "Урок 1. Появление цивилизаций"))
        self.shumer.setHtml(_translate("AncientFirstLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; font-style:italic; color:black; background-color:#ffe4b5;\">Шумерская цивилизация</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Arial,Helvetica,sans-serif\'; font-size:9pt; font-style:italic; color: black; background-color:#ffe4b5;\"> считается первой в истории человечества. Она возникла в долине рек Тигр и Евфрат (сейчас территория Ирака) примерно 6000 лет назад.</span></p></body></html>"))
        self.ancient_china.setHtml(_translate("AncientFirstLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; font-style:italic; color: black; background-color:#ffe4b5;\">Древний Китай</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Arial,Helvetica,sans-serif\'; font-size:9pt; font-style:italic; color: black; background-color:#ffe4b5;\">. Древнекитайская цивилизация зародилась на территории современного Китая в 5000 г. до н. э.. Развитию культуры способствовало активное земледелие в бассейнах рек Янцзы и Хуанхе.</span></p></body></html>"))
        self.first_civ_label.setText(_translate("AncientFirstLesson", "Первые цивилизации на Земле"))
        self.shumer_photo.setText(_translate("AncientFirstLesson", ""))
        self.china_photo.setText(_translate("AncientFirstLesson", ""))
        self.olmeki.setHtml(_translate("AncientFirstLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; font-style:italic; color: black; background-color:#ffe4b5;\">Ольмеки</span><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Arial,Helvetica,sans-serif\'; font-size:9pt; font-style:italic; color: black; background-color:#ffe4b5;\">. Археологическая культура, предшественник культуры майя. Зародилась в 2500 г. до н. э. на территории современной Мексики. Стала первой развитой цивилизацией в Центральной Америке</span></p></body></html>"))
        self.olmeki_photo.setText(_translate("AncientFirstLesson", ""))
        self.return_button.setText(_translate("AncientFirstLesson", "Вернуться назад"))
        self.next_lesson_button.setText(_translate("AncientFirstLesson", "Следующий урок"))
