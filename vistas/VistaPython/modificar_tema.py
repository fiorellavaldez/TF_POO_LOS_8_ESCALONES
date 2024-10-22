from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 640, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 9, 1061, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 210, 511, 421))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(10, 110, 1061, 51))
        self.listView_2.setObjectName("listView_2")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 640, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 110, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(740, 640, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(510, 209, 20, 421))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1040, 209, 20, 421))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.listView_3 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(550, 210, 511, 421))
        self.listView_3.setObjectName("listView_3")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 170, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.listView_4 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_4.setGeometry(QtCore.QRect(25, 220, 481, 151))
        self.listView_4.setObjectName("listView_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 471, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.listView_6 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_6.setGeometry(QtCore.QRect(555, 220, 481, 71))
        self.listView_6.setObjectName("listView_6")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(560, 250, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 220, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 580, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 580, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.listView_5 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_5.setGeometry(QtCore.QRect(25, 420, 481, 151))
        self.listView_5.setObjectName("listView_5")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 530, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 420, 471, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(950, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(860, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(860, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.listView_7 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_7.setGeometry(QtCore.QRect(555, 340, 481, 71))
        self.listView_7.setObjectName("listView_7")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(950, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(560, 370, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 340, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(860, 540, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.listView_8 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_8.setGeometry(QtCore.QRect(555, 460, 481, 71))
        self.listView_8.setObjectName("listView_8")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(950, 540, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(560, 490, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(560, 460, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.listView_3.raise_()
        self.listView.raise_()
        self.pushButton_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.listView_2.raise_()
        self.pushButton_12.raise_()
        self.label_2.raise_()
        self.pushButton_13.raise_()
        self.verticalScrollBar.raise_()
        self.label_3.raise_()
        self.verticalScrollBar_2.raise_()
        self.label_5.raise_()
        self.listView_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.listView_6.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.listView_5.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.listView_7.raise_()
        self.pushButton_10.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.pushButton_11.raise_()
        self.listView_8.raise_()
        self.pushButton_14.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Atrás"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Modificar Tema</span></p></body></html>"))
        self.pushButton_12.setText(_translate("MainWindow", "Agregar nueva pregunta de ronda"))
        self.label_2.setText(_translate("MainWindow", " Tema: Histora"))
        self.pushButton_13.setText(_translate("MainWindow", "Agregar nueva pregunta de desempate"))
        self.label_3.setText(_translate("MainWindow", "Preguntas de ronda"))
        self.label_5.setText(_translate("MainWindow", "Preguntas de desempate"))
        self.label_6.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?\n"
"a) Julio Cesar\n"
"b) Augusto\n"
"c)Nerón\n"
"d)Trajano"))
        self.label_7.setText(_translate("MainWindow", "Respuesta correcta: b)"))
        self.label_10.setText(_translate("MainWindow", "Respuesta correcta: 1453"))
        self.label_11.setText(_translate("MainWindow", "¿En qué año cayó Constantinopla?"))
        self.pushButton_3.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_4.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_5.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_6.setText(_translate("MainWindow", "Modificar"))
        self.label_8.setText(_translate("MainWindow", "Respuesta correcta: b)"))
        self.label_9.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?\n"
"a) Julio Cesar\n"
"b) Augusto\n"
"c)Nerón\n"
"d)Trajano"))
        self.pushButton_7.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_8.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_9.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_10.setText(_translate("MainWindow", "Eliminar"))
        self.label_12.setText(_translate("MainWindow", "Respuesta correcta: 1453"))
        self.label_13.setText(_translate("MainWindow", "¿En qué año cayó Constantinopla?"))
        self.pushButton_11.setText(_translate("MainWindow", "Modificar"))
        self.pushButton_14.setText(_translate("MainWindow", "Eliminar"))
        self.label_14.setText(_translate("MainWindow", "Respuesta correcta: 1453"))
        self.label_15.setText(_translate("MainWindow", "¿En qué año cayó Constantinopla?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())