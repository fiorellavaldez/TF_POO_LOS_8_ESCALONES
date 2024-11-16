from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1080, 720)
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
        self.listView.setGeometry(QtCore.QRect(10, 110, 1061, 521))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 640, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(990, 640, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView_2 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(20, 120, 1041, 111))
        self.listView_2.setObjectName("listView_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 541, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 200, 80, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(970, 200, 80, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.listView_3 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(20, 250, 1041, 111))
        self.listView_3.setObjectName("listView_3")
        self.listView_4 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_4.setGeometry(QtCore.QRect(20, 380, 1041, 111))
        self.listView_4.setObjectName("listView_4")
        self.listView_5 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_5.setGeometry(QtCore.QRect(20, 510, 1041, 111))
        self.listView_5.setObjectName("listView_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(870, 330, 80, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(970, 330, 80, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 541, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(870, 460, 80, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(970, 460, 80, 24))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 541, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(870, 590, 80, 24))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(970, 590, 80, 24))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 510, 541, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(660, 640, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Preguntas de historia</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_3.setText(_translate("MainWindow", ">"))
        self.label_2.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?  \n"
"a) Julio César\n"
"b) Augusto (CORRECTA)\n"
"c) Nerón\n"
"d) Trajano"))
        self.pushButton_4.setText(_translate("MainWindow", "Editar"))
        self.pushButton_5.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_6.setText(_translate("MainWindow", "Editar"))
        self.pushButton_7.setText(_translate("MainWindow", "Eliminar"))
        self.label_3.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?  \n"
"a) Julio César\n"
"b) Augusto (CORRECTA)\n"
"c) Nerón\n"
"d) Trajano"))
        self.pushButton_8.setText(_translate("MainWindow", "Editar"))
        self.pushButton_9.setText(_translate("MainWindow", "Eliminar"))
        self.label_4.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?  \n"
"a) Julio César\n"
"b) Augusto (CORRECTA)\n"
"c) Nerón\n"
"d) Trajano"))
        self.pushButton_10.setText(_translate("MainWindow", "Editar"))
        self.pushButton_11.setText(_translate("MainWindow", "Eliminar"))
        self.label_5.setText(_translate("MainWindow", "¿Quién fue el primer emperador de Roma?  \n"
"a) Julio César\n"
"b) Augusto (CORRECTA)\n"
"c) Nerón\n"
"d) Trajano"))
        self.pushButton_12.setText(_translate("MainWindow", "Agregar nueva pregunta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())