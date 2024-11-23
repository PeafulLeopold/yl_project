from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AncientSecondLesson(object):
    def setupUi(self, AncientSecondLesson):
        AncientSecondLesson.setObjectName("AncientSecondLesson")
        AncientSecondLesson.resize(1080, 852)
        self.centralwidget = QtWidgets.QWidget(parent=AncientSecondLesson)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading_label.setGeometry(QtCore.QRect(0, 0, 1041, 61))
        self.heading_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        self.introduction = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.introduction.setGeometry(QtCore.QRect(160, 100, 731, 111))
        self.introduction.setObjectName("introduction")
        self.ant_greece_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ant_greece_label.setGeometry(QtCore.QRect(10, 240, 681, 31))
        self.ant_greece_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ant_greece_label.setObjectName("ant_greece_label")
        self.ant_greece = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.ant_greece.setGeometry(QtCore.QRect(50, 270, 681, 111))
        self.ant_greece.setObjectName("ant_greece")
        self.ant_rome = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.ant_rome.setGeometry(QtCore.QRect(50, 430, 681, 121))
        self.ant_rome.setObjectName("ant_rome")
        self.ant_rome_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ant_rome_label.setGeometry(QtCore.QRect(10, 400, 681, 31))
        self.ant_rome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ant_rome_label.setObjectName("ant_rome_label")
        self.influence_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.influence_label.setGeometry(QtCore.QRect(0, 562, 1041, 31))
        self.influence_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.influence_label.setObjectName("influence_label")
        self.influence = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.influence.setGeometry(QtCore.QRect(160, 620, 731, 111))
        self.influence.setObjectName("influence")
        self.ant_greece_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.ant_greece_photo.setGeometry(QtCore.QRect(800, 260, 180, 120))
        self.ant_greece_photo.setObjectName("ant_greece_photo")
        self.ant_rome_photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.ant_rome_photo.setGeometry(QtCore.QRect(800, 430, 180, 121))
        self.ant_rome_photo.setObjectName("ant_rome_photo")
        self.return_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(440, 760, 171, 31))
        self.return_button.setObjectName("return_button")
        self.next_lesson_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_lesson_button.setGeometry(QtCore.QRect(640, 760, 141, 31))
        self.next_lesson_button.setObjectName("next_lesson_button")
        self.previous_lesson_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.previous_lesson_button.setGeometry(QtCore.QRect(270, 760, 141, 31))
        self.previous_lesson_button.setObjectName("previous_lesson_button")
        AncientSecondLesson.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AncientSecondLesson)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        AncientSecondLesson.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AncientSecondLesson)
        self.statusbar.setObjectName("statusbar")
        AncientSecondLesson.setStatusBar(self.statusbar)

        self.average_font = QtGui.QFont('Rockwell Extra Bold', 9)
        self.average_font.setBold(True)
        self.small_font = QtGui.QFont('Rockwell Extra Bold', 7)
        self.small_font.setBold(True)
        self.under_big_font = QtGui.QFont('Rockwell Extra Bold', 12)
        self.under_big_font.setBold(True)
        self.big_font = QtGui.QFont('Rockwell Extra Bold', 16)
        self.big_font.setBold(True)

        self.ant_greece_label.setFont(self.average_font)
        self.ant_rome_label.setFont(self.average_font)
        self.return_button.setFont(self.small_font)
        self.next_lesson_button.setFont(self.small_font)
        self.previous_lesson_button.setFont(self.small_font)
        self.heading_label.setFont(self.big_font)
        self.influence_label.setFont(self.under_big_font)

        self.ant_rome_photo.setPixmap(QtGui.QPixmap('data/lessons_photo/ancient_world/coleseum.webp'))
        self.ant_greece_photo.setPixmap(QtGui.QPixmap('data/lessons_photo/ancient_world/parphenon.webp'))

        self.ant_rome_photo.setScaledContents(True)
        self.ant_greece_photo.setScaledContents(True)

        self.parphenon_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.parphenon_label.setGeometry(QtCore.QRect(820, 380, 180, 20))
        self.parphenon_label.setText('Парфенон в Древней Греции')
        self.parphenon_label.setFont(self.small_font)

        self.coleseum_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.coleseum_label.setGeometry(QtCore.QRect(830, 550, 180, 20))
        self.coleseum_label.setText('Колизей в Древнем Риме')
        self.coleseum_label.setFont(self.small_font)

        self.widgets = [self.heading_label, self.influence_label, self.ant_greece_label,
                        self.ant_rome_label, self.return_button, self.next_lesson_button,
                        self.previous_lesson_button]


        self.retranslateUi(AncientSecondLesson)
        QtCore.QMetaObject.connectSlotsByName(AncientSecondLesson)

    def retranslateUi(self, AncientSecondLesson):
        _translate = QtCore.QCoreApplication.translate
        AncientSecondLesson.setWindowTitle(_translate("AncientSecondLesson", "AncientSecondLesson"))
        self.heading_label.setText(_translate("AncientSecondLesson", "Античная Греция и Рим"))
        self.introduction.setHtml(_translate("AncientSecondLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Античная Греция и Рим</span><span style=\" font-size:11pt;\"> —</span><span style=\" font-size:11pt; font-style:italic;\"> это две великие цивилизации, которые оказали значительное влияние на развитие культуры, философии, искусства и политики в мире. Они заложили основы многих современных наук и форм правления.</span></p></body></html>"))
        self.ant_greece_label.setText(_translate("AncientSecondLesson", "Античная Греция"))
        self.ant_greece.setHtml(_translate("AncientSecondLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Античная Греция</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-style:italic;\">(около VIII века до н.э. — IV век н.э.) известна своими городами-государствами, такими как Афины и Спарта. Афины стали центром демократии и культуры, где развивались философия (Сократ, Платон, Аристотель), театр (Эсхил, Софокл) и изобразительное искусство (скульптуры Фидия). Спарта славилась своим военным делом и строгой системой воспитания.</span></p></body></html>"))
        self.ant_rome.setHtml(_translate("AncientSecondLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Римская цивилизация</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-style:italic;\">(около VIII века до н.э. — V век н.э.) начала как небольшое поселение и выросла в огромную империю. Римляне создали эффективную систему управления, права и архитектуры. Они построили акведуки, дороги и величественные здания, такие как Колизей и Пантеон. Римское право стало основой для многих современных правовых систем.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p></body></html>"))
        self.ant_rome_label.setText(_translate("AncientSecondLesson", "Античный Рим"))
        self.influence_label.setText(_translate("AncientSecondLesson", "Влияние на современность"))
        self.influence.setHtml(_translate("AncientSecondLesson", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.2pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Культура и идеи античных цивилизаций продолжают оказывать влияние на современное общество. Мы используем греческие термины в науке и искусстве, а римское право является основой для юридических систем многих стран.</span></p></body></html>"))
        self.ant_greece_photo.setText(_translate("AncientSecondLesson", ""))
        self.ant_rome_photo.setText(_translate("AncientSecondLesson", ""))
        self.return_button.setText(_translate("AncientSecondLesson", "Вернуться назад"))
        self.next_lesson_button.setText(_translate("AncientSecondLesson", "Следующий урок"))
        self.previous_lesson_button.setText(_translate("AncientSecondLesson", "Прошлый урок"))
