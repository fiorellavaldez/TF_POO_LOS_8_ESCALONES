# Form implementation generated from reading ui file 'VistaJuego.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 673)
        MainWindow.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 150, 951, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_escalon3 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon3.sizePolicy().hasHeightForWidth())
        self.widget_escalon3.setSizePolicy(sizePolicy)
        self.widget_escalon3.setMaximumSize(QtCore.QSize(550, 60))
        self.widget_escalon3.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon3.setObjectName("widget_escalon3")
        self.numero_escalon8 = QtWidgets.QLabel(parent=self.widget_escalon3)
        self.numero_escalon8.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon8.sizePolicy().hasHeightForWidth())
        self.numero_escalon8.setSizePolicy(sizePolicy)
        self.numero_escalon8.setText("")
        self.numero_escalon8.setPixmap(QtGui.QPixmap("vista/img/number-8-circle-svgrepo-com.png"))
        self.numero_escalon8.setScaledContents(True)
        self.numero_escalon8.setObjectName("numero_escalon8")
        self.label_tematica8 = QtWidgets.QLabel(parent=self.widget_escalon3)
        self.label_tematica8.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica8.setFont(font)
        self.label_tematica8.setObjectName("label_tematica8")
        self.verticalLayout.addWidget(self.widget_escalon3)
        self.widget_escalon7 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon7.sizePolicy().hasHeightForWidth())
        self.widget_escalon7.setSizePolicy(sizePolicy)
        self.widget_escalon7.setMaximumSize(QtCore.QSize(600, 60))
        self.widget_escalon7.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon7.setObjectName("widget_escalon7")
        self.numero_escalon7 = QtWidgets.QLabel(parent=self.widget_escalon7)
        self.numero_escalon7.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon7.sizePolicy().hasHeightForWidth())
        self.numero_escalon7.setSizePolicy(sizePolicy)
        self.numero_escalon7.setText("")
        self.numero_escalon7.setPixmap(QtGui.QPixmap("vista/img/number-7-circle-svgrepo-com.png"))
        self.numero_escalon7.setScaledContents(True)
        self.numero_escalon7.setObjectName("numero_escalon7")
        self.label_tematica7 = QtWidgets.QLabel(parent=self.widget_escalon7)
        self.label_tematica7.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica7.setFont(font)
        self.label_tematica7.setObjectName("label_tematica7")
        self.verticalLayout.addWidget(self.widget_escalon7)
        self.widget_escalon6 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon6.sizePolicy().hasHeightForWidth())
        self.widget_escalon6.setSizePolicy(sizePolicy)
        self.widget_escalon6.setMaximumSize(QtCore.QSize(650, 60))
        self.widget_escalon6.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon6.setObjectName("widget_escalon6")
        self.numero_escalon6 = QtWidgets.QLabel(parent=self.widget_escalon6)
        self.numero_escalon6.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon6.sizePolicy().hasHeightForWidth())
        self.numero_escalon6.setSizePolicy(sizePolicy)
        self.numero_escalon6.setText("")
        self.numero_escalon6.setPixmap(QtGui.QPixmap("vista/img/number-6-circle-svgrepo-com.png"))
        self.numero_escalon6.setScaledContents(True)
        self.numero_escalon6.setObjectName("numero_escalon6")
        self.label_tematica6 = QtWidgets.QLabel(parent=self.widget_escalon6)
        self.label_tematica6.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica6.setFont(font)
        self.label_tematica6.setObjectName("label_tematica6")
        self.verticalLayout.addWidget(self.widget_escalon6)
        self.widget_escalon5 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon5.sizePolicy().hasHeightForWidth())
        self.widget_escalon5.setSizePolicy(sizePolicy)
        self.widget_escalon5.setMaximumSize(QtCore.QSize(700, 60))
        self.widget_escalon5.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon5.setObjectName("widget_escalon5")
        self.numero_escalon5 = QtWidgets.QLabel(parent=self.widget_escalon5)
        self.numero_escalon5.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon5.sizePolicy().hasHeightForWidth())
        self.numero_escalon5.setSizePolicy(sizePolicy)
        self.numero_escalon5.setText("")
        self.numero_escalon5.setPixmap(QtGui.QPixmap("vista/img/number-5-circle-svgrepo-com.png"))
        self.numero_escalon5.setScaledContents(True)
        self.numero_escalon5.setObjectName("numero_escalon5")
        self.label_tematica5 = QtWidgets.QLabel(parent=self.widget_escalon5)
        self.label_tematica5.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica5.setFont(font)
        self.label_tematica5.setObjectName("label_tematica5")
        self.verticalLayout.addWidget(self.widget_escalon5)
        self.widget_escalon9 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon9.sizePolicy().hasHeightForWidth())
        self.widget_escalon9.setSizePolicy(sizePolicy)
        self.widget_escalon9.setMaximumSize(QtCore.QSize(750, 60))
        self.widget_escalon9.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon9.setObjectName("widget_escalon9")
        self.numero_escalon4 = QtWidgets.QLabel(parent=self.widget_escalon9)
        self.numero_escalon4.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon4.sizePolicy().hasHeightForWidth())
        self.numero_escalon4.setSizePolicy(sizePolicy)
        self.numero_escalon4.setText("")
        self.numero_escalon4.setPixmap(QtGui.QPixmap("vista/img/number-4-circle-svgrepo-com.png"))
        self.numero_escalon4.setScaledContents(True)
        self.numero_escalon4.setObjectName("numero_escalon4")
        self.label_tematica4 = QtWidgets.QLabel(parent=self.widget_escalon9)
        self.label_tematica4.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica4.setFont(font)
        self.label_tematica4.setObjectName("label_tematica4")
        self.verticalLayout.addWidget(self.widget_escalon9)
        self.widget_escalon4 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon4.sizePolicy().hasHeightForWidth())
        self.widget_escalon4.setSizePolicy(sizePolicy)
        self.widget_escalon4.setMaximumSize(QtCore.QSize(800, 60))
        self.widget_escalon4.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon4.setObjectName("widget_escalon4")
        self.numero_escalon3 = QtWidgets.QLabel(parent=self.widget_escalon4)
        self.numero_escalon3.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon3.sizePolicy().hasHeightForWidth())
        self.numero_escalon3.setSizePolicy(sizePolicy)
        self.numero_escalon3.setText("")
        self.numero_escalon3.setPixmap(QtGui.QPixmap("vista/img/number-3-circle-svgrepo-com.png"))
        self.numero_escalon3.setScaledContents(True)
        self.numero_escalon3.setObjectName("numero_escalon3")
        self.label_tematica3 = QtWidgets.QLabel(parent=self.widget_escalon4)
        self.label_tematica3.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica3.setFont(font)
        self.label_tematica3.setObjectName("label_tematica3")
        self.verticalLayout.addWidget(self.widget_escalon4)
        self.widget_escalon2 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon2.sizePolicy().hasHeightForWidth())
        self.widget_escalon2.setSizePolicy(sizePolicy)
        self.widget_escalon2.setMaximumSize(QtCore.QSize(850, 60))
        self.widget_escalon2.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon2.setObjectName("widget_escalon2")
        self.numero_escalon2 = QtWidgets.QLabel(parent=self.widget_escalon2)
        self.numero_escalon2.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon2.sizePolicy().hasHeightForWidth())
        self.numero_escalon2.setSizePolicy(sizePolicy)
        self.numero_escalon2.setText("")
        self.numero_escalon2.setPixmap(QtGui.QPixmap("vista/img/number-2-circle-svgrepo-com.png"))
        self.numero_escalon2.setScaledContents(True)
        self.numero_escalon2.setObjectName("numero_escalon2")
        self.label_tematica2 = QtWidgets.QLabel(parent=self.widget_escalon2)
        self.label_tematica2.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica2.setFont(font)
        self.label_tematica2.setObjectName("label_tematica2")
        self.verticalLayout.addWidget(self.widget_escalon2)
        self.widget_escalon1 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_escalon1.sizePolicy().hasHeightForWidth())
        self.widget_escalon1.setSizePolicy(sizePolicy)
        self.widget_escalon1.setMaximumSize(QtCore.QSize(900, 60))
        self.widget_escalon1.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.widget_escalon1.setObjectName("widget_escalon1")
        self.numero_escalon1 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.numero_escalon1.setGeometry(QtCore.QRect(0, 0, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numero_escalon1.sizePolicy().hasHeightForWidth())
        self.numero_escalon1.setSizePolicy(sizePolicy)
        self.numero_escalon1.setText("")
        self.numero_escalon1.setPixmap(QtGui.QPixmap("vista/img/number-1-circle-svgrepo-com.png"))
        self.numero_escalon1.setScaledContents(True)
        self.numero_escalon1.setObjectName("numero_escalon1")
        self.icono_jugador9 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador9.setGeometry(QtCore.QRect(830, 0, 31, 31))
        self.icono_jugador9.setText("")
        self.icono_jugador9.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador9.setScaledContents(True)
        self.icono_jugador9.setObjectName("icono_jugador9")
        self.icono_jugador8 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador8.setGeometry(QtCore.QRect(770, 0, 31, 31))
        self.icono_jugador8.setText("")
        self.icono_jugador8.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador8.setScaledContents(True)
        self.icono_jugador8.setObjectName("icono_jugador8")
        self.icono_jugador6 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador6.setGeometry(QtCore.QRect(650, 0, 31, 31))
        self.icono_jugador6.setText("")
        self.icono_jugador6.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador6.setScaledContents(True)
        self.icono_jugador6.setObjectName("icono_jugador6")
        self.icono_jugador7 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador7.setGeometry(QtCore.QRect(710, 0, 31, 31))
        self.icono_jugador7.setText("")
        self.icono_jugador7.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador7.setScaledContents(True)
        self.icono_jugador7.setObjectName("icono_jugador7")
        self.icono_jugador5 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador5.setGeometry(QtCore.QRect(590, 0, 31, 31))
        self.icono_jugador5.setText("")
        self.icono_jugador5.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador5.setScaledContents(True)
        self.icono_jugador5.setObjectName("icono_jugador5")
        self.icono_jugador4 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador4.setGeometry(QtCore.QRect(530, 0, 31, 31))
        self.icono_jugador4.setText("")
        self.icono_jugador4.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador4.setScaledContents(True)
        self.icono_jugador4.setObjectName("icono_jugador4")
        self.icono_jugador3 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador3.setGeometry(QtCore.QRect(470, 0, 31, 31))
        self.icono_jugador3.setText("")
        self.icono_jugador3.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador3.setScaledContents(True)
        self.icono_jugador3.setObjectName("icono_jugador3")
        self.icono_jugador2 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador2.setGeometry(QtCore.QRect(410, 0, 31, 31))
        self.icono_jugador2.setText("")
        self.icono_jugador2.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador2.setScaledContents(True)
        self.icono_jugador2.setObjectName("icono_jugador2")
        self.icono_jugador1 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.icono_jugador1.setGeometry(QtCore.QRect(350, 0, 31, 31))
        self.icono_jugador1.setText("")
        self.icono_jugador1.setPixmap(QtGui.QPixmap("vista/img/icono_verde.png"))
        self.icono_jugador1.setScaledContents(True)
        self.icono_jugador1.setObjectName("icono_jugador1")
        self.label_tematica1 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_tematica1.setGeometry(QtCore.QRect(70, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(18)
        self.label_tematica1.setFont(font)
        self.label_tematica1.setObjectName("label_tematica1")
        self.label_jugador1 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador1.setGeometry(QtCore.QRect(340, 30, 49, 16))
        self.label_jugador1.setObjectName("label_jugador1")
        self.checkBox_jugador1_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador1_rd1.setEnabled(False)
        self.checkBox_jugador1_rd1.setGeometry(QtCore.QRect(350, 50, 12, 8))
        self.checkBox_jugador1_rd1.setText("")
        self.checkBox_jugador1_rd1.setCheckable(False)
        self.checkBox_jugador1_rd1.setObjectName("checkBox_jugador1_rd1")
        self.checkBox_jugador1_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador1_rd2.setEnabled(False)
        self.checkBox_jugador1_rd2.setGeometry(QtCore.QRect(368, 50, 12, 8))
        self.checkBox_jugador1_rd2.setText("")
        self.checkBox_jugador1_rd2.setCheckable(False)
        self.checkBox_jugador1_rd2.setObjectName("checkBox_jugador1_rd2")
        self.checkBox_jugador2_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador2_rd1.setEnabled(False)
        self.checkBox_jugador2_rd1.setGeometry(QtCore.QRect(410, 50, 12, 8))
        self.checkBox_jugador2_rd1.setText("")
        self.checkBox_jugador2_rd1.setCheckable(False)
        self.checkBox_jugador2_rd1.setObjectName("checkBox_jugador2_rd1")
        self.checkBox_jugador2_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador2_rd2.setEnabled(False)
        self.checkBox_jugador2_rd2.setGeometry(QtCore.QRect(428, 50, 12, 8))
        self.checkBox_jugador2_rd2.setText("")
        self.checkBox_jugador2_rd2.setCheckable(False)
        self.checkBox_jugador2_rd2.setObjectName("checkBox_jugador2_rd2")
        self.label_jugador2 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador2.setGeometry(QtCore.QRect(400, 30, 49, 16))
        self.label_jugador2.setObjectName("label_jugador2")
        self.checkBox_jugador3_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador3_rd1.setEnabled(False)
        self.checkBox_jugador3_rd1.setGeometry(QtCore.QRect(470, 50, 12, 8))
        self.checkBox_jugador3_rd1.setText("")
        self.checkBox_jugador3_rd1.setCheckable(False)
        self.checkBox_jugador3_rd1.setObjectName("checkBox_jugador3_rd1")
        self.checkBox_jugador3_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador3_rd2.setEnabled(False)
        self.checkBox_jugador3_rd2.setGeometry(QtCore.QRect(488, 50, 12, 8))
        self.checkBox_jugador3_rd2.setText("")
        self.checkBox_jugador3_rd2.setCheckable(False)
        self.checkBox_jugador3_rd2.setObjectName("checkBox_jugador3_rd2")
        self.label_jugador3 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador3.setGeometry(QtCore.QRect(460, 30, 49, 16))
        self.label_jugador3.setObjectName("label_jugador3")
        self.checkBox_jugador4_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador4_rd1.setEnabled(False)
        self.checkBox_jugador4_rd1.setGeometry(QtCore.QRect(530, 50, 12, 8))
        self.checkBox_jugador4_rd1.setText("")
        self.checkBox_jugador4_rd1.setCheckable(False)
        self.checkBox_jugador4_rd1.setObjectName("checkBox_jugador4_rd1")
        self.checkBox_jugador4_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador4_rd2.setEnabled(False)
        self.checkBox_jugador4_rd2.setGeometry(QtCore.QRect(548, 50, 12, 8))
        self.checkBox_jugador4_rd2.setText("")
        self.checkBox_jugador4_rd2.setCheckable(False)
        self.checkBox_jugador4_rd2.setObjectName("checkBox_jugador4_rd2")
        self.label_jugador4 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador4.setGeometry(QtCore.QRect(520, 30, 49, 16))
        self.label_jugador4.setObjectName("label_jugador4")
        self.checkBox_jugador5_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador5_rd1.setEnabled(False)
        self.checkBox_jugador5_rd1.setGeometry(QtCore.QRect(590, 50, 12, 8))
        self.checkBox_jugador5_rd1.setText("")
        self.checkBox_jugador5_rd1.setCheckable(False)
        self.checkBox_jugador5_rd1.setObjectName("checkBox_jugador5_rd1")
        self.checkBox_jugador5_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador5_rd2.setEnabled(False)
        self.checkBox_jugador5_rd2.setGeometry(QtCore.QRect(608, 50, 12, 8))
        self.checkBox_jugador5_rd2.setText("")
        self.checkBox_jugador5_rd2.setCheckable(False)
        self.checkBox_jugador5_rd2.setObjectName("checkBox_jugador5_rd2")
        self.label_jugador5 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador5.setGeometry(QtCore.QRect(580, 30, 49, 16))
        self.label_jugador5.setObjectName("label_jugador5")
        self.checkBox_jugador6_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador6_rd1.setEnabled(False)
        self.checkBox_jugador6_rd1.setGeometry(QtCore.QRect(650, 50, 12, 8))
        self.checkBox_jugador6_rd1.setText("")
        self.checkBox_jugador6_rd1.setCheckable(False)
        self.checkBox_jugador6_rd1.setObjectName("checkBox_jugador6_rd1")
        self.checkBox_jugador6_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador6_rd2.setEnabled(False)
        self.checkBox_jugador6_rd2.setGeometry(QtCore.QRect(668, 50, 12, 8))
        self.checkBox_jugador6_rd2.setText("")
        self.checkBox_jugador6_rd2.setCheckable(False)
        self.checkBox_jugador6_rd2.setObjectName("checkBox_jugador6_rd2")
        self.label_jugador6 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador6.setGeometry(QtCore.QRect(640, 30, 49, 16))
        self.label_jugador6.setObjectName("label_jugador6")
        self.checkBox_jugador7_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador7_rd1.setEnabled(False)
        self.checkBox_jugador7_rd1.setGeometry(QtCore.QRect(710, 50, 12, 8))
        self.checkBox_jugador7_rd1.setText("")
        self.checkBox_jugador7_rd1.setCheckable(False)
        self.checkBox_jugador7_rd1.setObjectName("checkBox_jugador7_rd1")
        self.checkBox_jugador7_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador7_rd2.setEnabled(False)
        self.checkBox_jugador7_rd2.setGeometry(QtCore.QRect(728, 50, 12, 8))
        self.checkBox_jugador7_rd2.setText("")
        self.checkBox_jugador7_rd2.setCheckable(False)
        self.checkBox_jugador7_rd2.setObjectName("checkBox_jugador7_rd2")
        self.label_jugador7 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador7.setGeometry(QtCore.QRect(700, 30, 49, 16))
        self.label_jugador7.setObjectName("label_jugador7")
        self.checkBox_jugador8_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador8_rd1.setEnabled(False)
        self.checkBox_jugador8_rd1.setGeometry(QtCore.QRect(770, 50, 12, 8))
        self.checkBox_jugador8_rd1.setText("")
        self.checkBox_jugador8_rd1.setCheckable(False)
        self.checkBox_jugador8_rd1.setObjectName("checkBox_jugador8_rd1")
        self.checkBox_jugador8_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador8_rd2.setEnabled(False)
        self.checkBox_jugador8_rd2.setGeometry(QtCore.QRect(788, 50, 12, 8))
        self.checkBox_jugador8_rd2.setText("")
        self.checkBox_jugador8_rd2.setCheckable(False)
        self.checkBox_jugador8_rd2.setObjectName("checkBox_jugador8_rd2")
        self.label_jugador8 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador8.setGeometry(QtCore.QRect(760, 30, 49, 16))
        self.label_jugador8.setObjectName("label_jugador8")
        self.checkBox_jugador9_rd1 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador9_rd1.setEnabled(False)
        self.checkBox_jugador9_rd1.setGeometry(QtCore.QRect(830, 50, 12, 8))
        self.checkBox_jugador9_rd1.setText("")
        self.checkBox_jugador9_rd1.setCheckable(False)
        self.checkBox_jugador9_rd1.setObjectName("checkBox_jugador9_rd1")
        self.checkBox_jugador9_rd2 = QtWidgets.QCheckBox(parent=self.widget_escalon1)
        self.checkBox_jugador9_rd2.setEnabled(False)
        self.checkBox_jugador9_rd2.setGeometry(QtCore.QRect(848, 50, 12, 8))
        self.checkBox_jugador9_rd2.setText("")
        self.checkBox_jugador9_rd2.setCheckable(False)
        self.checkBox_jugador9_rd2.setObjectName("checkBox_jugador9_rd2")
        self.label_jugador9 = QtWidgets.QLabel(parent=self.widget_escalon1)
        self.label_jugador9.setGeometry(QtCore.QRect(820, 30, 49, 16))
        self.label_jugador9.setObjectName("label_jugador9")
        self.verticalLayout.addWidget(self.widget_escalon1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 30, 191, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("vista/img/ganador-triunfador.gif"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton_atras = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_atras.setGeometry(QtCore.QRect(10, 640, 75, 24))
        self.pushButton_atras.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_atras.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_atras.setObjectName("pushButton_atras")
        self.pushButton_pregunta = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_pregunta.setGeometry(QtCore.QRect(100, 640, 75, 24))
        self.pushButton_pregunta.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_pregunta.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_pregunta.setObjectName("pushButton_pregunta")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.centralwidget.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_tematica8.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_tematica7.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_tematica6.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_tematica5.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_tematica4.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_tematica3.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_tematica2.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_tematica1.setText(_translate("MainWindow", "GEOGRAFIA"))
        self.label_jugador1.setText(_translate("MainWindow", "jugador1"))
        self.label_jugador2.setText(_translate("MainWindow", "jugador2"))
        self.label_jugador3.setText(_translate("MainWindow", "jugador3"))
        self.label_jugador4.setText(_translate("MainWindow", "jugador4"))
        self.label_jugador5.setText(_translate("MainWindow", "jugador5"))
        self.label_jugador6.setText(_translate("MainWindow", "jugador6"))
        self.label_jugador7.setText(_translate("MainWindow", "jugador7"))
        self.label_jugador8.setText(_translate("MainWindow", "jugador8"))
        self.label_jugador9.setText(_translate("MainWindow", "jugador9"))
        self.pushButton_atras.setText(_translate("MainWindow", "Atras"))
        self.pushButton_pregunta.setText(_translate("MainWindow", "Pregunta"))

    def get_button_atras(self):
        return self.pushButton_atras

    def get_button_pregunta(self):
        return self.pushButton_pregunta


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
