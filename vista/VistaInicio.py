from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 721, 241))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 290, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 380, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 470, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 560, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">Los 8 escalones</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Nueva Partida"))
        self.pushButton_4.setText(_translate("MainWindow", "Continuar"))
        self.pushButton_5.setText(_translate("MainWindow", "Configuracion"))
        self.pushButton_6.setText(_translate("MainWindow", "Salir"))

    def get_button_configuracion(self):
        return self.pushButton_5 # estaría bien renombrar los 'pushButton_5' para saber de qué es el botón
    
    def get_button_nueva_partida(self):
        return self.pushButton
    
    def get_button_salir(self):
        return self.pushButton_6