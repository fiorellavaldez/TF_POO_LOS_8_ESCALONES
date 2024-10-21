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
        self.listView.setGeometry(QtCore.QRect(20, 260, 511, 371))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(20, 120, 1041, 111))
        self.listView_2.setObjectName("listView_2")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(410, 640, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 130, 541, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 130, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 180, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(750, 640, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(510, 259, 20, 371))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(parent=self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1040, 259, 20, 371))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.listView_3 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(550, 260, 511, 371))
        self.listView_3.setObjectName("listView_3")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(710, 230, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.listView_4 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_4.setGeometry(QtCore.QRect(25, 270, 481, 151))
        self.listView_4.setObjectName("listView_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 471, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 380, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.listView_5 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_5.setGeometry(QtCore.QRect(25, 430, 481, 151))
        self.listView_5.setObjectName("listView_5")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 540, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 430, 471, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.listView_6 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_6.setGeometry(QtCore.QRect(555, 270, 481, 71))
        self.listView_6.setObjectName("listView_6")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(560, 300, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 270, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.listView_3.raise_()
        self.listView.raise_()
        self.pushButton_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.listView_2.raise_()
        self.pushButton_12.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.pushButton_4.raise_()
        self.label_4.raise_()
        self.pushButton_13.raise_()
        self.verticalScrollBar.raise_()
        self.label_3.raise_()
        self.verticalScrollBar_2.raise_()
        self.label_5.raise_()
        self.listView_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.listView_5.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.listView_6.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Tema Nuevo</span></p></body></html>"))
        self.pushButton_12.setText(_translate("MainWindow", "Agregar nueva pregunta de ronda"))
        self.label_2.setText(_translate("MainWindow", "Nombre del Tema"))
        self.pushButton_4.setText(_translate("MainWindow", "Agregar"))
        self.label_4.setText(_translate("MainWindow", "Una vez agregado el tema, haga click en \"Agregar nueva pregunta de ronda\" o \"Agregar nueva pregunta de desempate\""))
        self.pushButton_13.setText(_translate("MainWindow", "Agregar nueva pregunta de desempate"))
        self.label_3.setText(_translate("MainWindow", "Preguntas de ronda"))
        self.label_5.setText(_translate("MainWindow", "Preguntas de desempate"))
        self.label_6.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?\n"
"a) Julio Cesar\n"
"b) Augusto\n"
"c)Nerón\n"
"d)Trajano"))
        self.label_7.setText(_translate("MainWindow", "Respuesta correcta: b)"))
        self.label_8.setText(_translate("MainWindow", "Respuesta correcta: b)"))
        self.label_9.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?\n"
"a) Julio Cesar\n"
"b) Augusto\n"
"c)Nerón\n"
"d)Trajano"))
        self.label_10.setText(_translate("MainWindow", "Respuesta correcta: 1453"))
        self.label_11.setText(_translate("MainWindow", "¿En qué año cayó Constantinopla?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())