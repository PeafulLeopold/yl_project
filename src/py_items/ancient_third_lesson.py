from PyQt6.QtGui import QFont
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AncientThirdLesson(object):
    def setupUi(self, AncientThirdLesson):
        AncientThirdLesson.setObjectName("AncientThirdLesson")
        AncientThirdLesson.resize(1101, 937)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        AncientThirdLesson.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=AncientThirdLesson)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(0, 0, 1101, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.heading_label.setFont(font)
        self.heading_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        self.inroduction_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.inroduction_label.setGeometry(QtCore.QRect(0, 102, 1101, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inroduction_label.setFont(font)
        self.inroduction_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inroduction_label.setObjectName("inroduction_label")
        self.introduction = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.introduction.setGeometry(QtCore.QRect(120, 180, 861, 131))
        self.introduction.setObjectName("introduction")
        self.religion_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.religion_label.setGeometry(QtCore.QRect(0, 340, 1101, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.religion_label.setFont(font)
        self.religion_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.religion_label.setObjectName("religion_label")
        self.religion = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.religion.setGeometry(QtCore.QRect(120, 410, 861, 161))
        self.religion.setObjectName("religion")
        self.philosophy_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.philosophy_label.setGeometry(QtCore.QRect(0, 610, 1101, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.philosophy_label.setFont(font)
        self.philosophy_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.philosophy_label.setObjectName("philosophy_label")
        self.philosophy = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.philosophy.setGeometry(QtCore.QRect(120, 660, 861, 161))
        self.philosophy.setObjectName("philosophy")
        self.previous_lesson_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.previous_lesson_button.setGeometry(QtCore.QRect(310, 840, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.previous_lesson_button.setFont(font)
        self.previous_lesson_button.setObjectName("previous_lesson_button")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(480, 840, 141, 41))
        self.return_button.setObjectName("return_button")
        self.next_lesson_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_lesson_button.setGeometry(QtCore.QRect(650, 840, 141, 41))
        self.next_lesson_button.setObjectName("next_lesson_button")
        AncientThirdLesson.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AncientThirdLesson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 21))
        self.menubar.setObjectName("menubar")
        AncientThirdLesson.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AncientThirdLesson)
        self.statusbar.setObjectName("statusbar")
        AncientThirdLesson.setStatusBar(self.statusbar)

        self.small_font = QFont('Rockwell Extra Bold', 8)
        self.average_font = QFont('Rockwell Extra Bold', 9)
        self.big_font = QFont('Rockwell Extra Bold', 14)
        self.under_big_font = QFont('Rockwell Extra Bold', 12)
        self.under_big_font.setBold(True)
        self.small_font.setBold(True)
        self.average_font.setBold(True)
        self.big_font.setBold(True)

        self.heading_label.setFont(self.big_font)
        self.inroduction_label.setFont(self.under_big_font)
        self.religion_label.setFont(self.average_font)
        self.philosophy_label.setFont(self.average_font)
        self.next_lesson_button.setFont(self.small_font)
        self.previous_lesson_button.setFont(self.small_font)
        self.return_button.setFont(self.small_font)


        self.retranslateUi(AncientThirdLesson)
        QtCore.QMetaObject.connectSlotsByName(AncientThirdLesson)

    def retranslateUi(self, AncientThirdLesson):
        _translate = QtCore.QCoreApplication.translate
        AncientThirdLesson.setWindowTitle(_translate("AncientThirdLesson", "AncientThirdLesson"))
        self.heading_label.setText(_translate("AncientThirdLesson", "Религиозные и философские учения древней эпохи"))
        self.inroduction_label.setText(_translate("AncientThirdLesson", "Введение"))
        self.introduction.setHtml(_translate("AncientThirdLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell Extra Bold\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:italic;\">Древний мир был насыщен разнообразными религиозными и философскими учениями, которые формировали мировоззрение людей и оказывали влияние на их поведение и общественные структуры. В этом уроке мы рассмотрим основные религии и философские системы, существовавшие в Древнем Египте, Месопотамии, Индии, Китае и Греции.</span></p></body></html>"))
        self.religion_label.setText(_translate("AncientThirdLesson", "Религиозные учения разных стран"))
        self.religion.setHtml(_translate("AncientThirdLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell Extra Bold\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\">• Древний Египет: Политеизм с поклонением богам, таким как Ра и Осирис. Религия была связана с природными циклами и загробной жизнью. Пирамиды служили местами поклонения.  </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\">• Месопотамия: Вавилоняне и шумеры имели богов, управлявших жизнью, как Мардук и Инанна. Мифы, например, «Эпос о Гильгамеше», отражали их взгляды на жизнь и смерть.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\">• Индийские религии: Индуизм с верой в карму и реинкарнацию, а буддизм, основанный на учениях Будды, акцентирует внимание на пути к просветлению.</span></p></body></html>"))
        self.philosophy_label.setText(_translate("AncientThirdLesson", "Философские учения разных стран"))
        self.philosophy.setHtml(_translate("AncientThirdLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell Extra Bold\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\">• Древний Китай: Конфуцианство, акцентирующее мораль и социальную гармонию, и даосизм, подчеркивающий единство с природой.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\">  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:italic;\">• Древняя Греция: Философы, такие как Сократ, Платон и Аристотель, заложили основы западной философии. Сократ задавал вопросы о добродетели, Платон развивал идеи о мире идей, а Аристотель исследовал природу реальности и этики.</span></p></body></html>"))
        self.previous_lesson_button.setText(_translate("AncientThirdLesson", "Прошлый урок"))
        self.return_button.setText(_translate("AncientThirdLesson", "Назад"))
        self.next_lesson_button.setText(_translate("AncientThirdLesson", "Следующий урок"))
