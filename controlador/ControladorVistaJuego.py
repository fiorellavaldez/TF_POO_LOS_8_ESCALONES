from vista.VistaJuego import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox, QDialog, QLabel, QPushButton
from PyQt6.QtGui import QFont

class ControladorVistaJuego:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        #traer Tema y ahí están las preguntas
        #self.Tema = Tema() creo que en un metodo
        


        
        self.__vista.get_button_atras().clicked.connect(self.__atras)
        self.__vista.get_button_pregunta().clicked.connect(self.__obtener_pregunta)

    def __atras(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    #def pregunta (Self):
        # lista_preguntas = self.tema.preguntas_ronda
        #for i in lista_preguntas:
            #self.Dialog(pregunta, a, b, c, d, correcta)

            #Dialog
            # labelpregunta.setText(pregunta)
            # if boton_a.getText() == correcta:
            #     boton_a.clicked.connect(self.carte_correcto)

            #     boton_a.clicked.getText() == correcta:
            #         self.cartel_correcto()

            #     while sdksds

            #     break
        

    def __obtener_pregunta(self): #pasarlo a una vista y la llamamos acá
        dlg = QDialog()
        dlg.resize(599, 444)
        dlg.setWindowTitle("Pregunta!")

        #fonts
        font_14b = QFont()
        font_14b.setPointSize(14)
        font_14b.setBold(True)

        font_14 = QFont()
        font_14b.setPointSize(14)

        font_15b = QFont()
        font_15b.setPointSize(15)
        font_15b.setBold(True)

        font_11b = QFont()
        font_11b.setPointSize(11)
        font_11b.setBold(True)

        font_11 = QFont()
        font_11.setPointSize(11)

        #pregunta
        pregunta = QLabel("Pregunta", dlg) #necesita setText
        pregunta.setGeometry(QtCore.QRect(20, 110, 561, 71))
        pregunta.setFont(font_15b)
        pregunta.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        pregunta.setWordWrap(True)

        #jugador
        jugador_label = QLabel("Jugador:", dlg)
        jugador_label.setGeometry(QtCore.QRect(310, 50, 91, 31))   
        jugador_label.setFont(font_14b)
        nombre_jugador = QLabel("Nombre",dlg) #necesita setText
        nombre_jugador.setFont(font_14)
        nombre_jugador.setGeometry(QtCore.QRect(400, 60, 121, 16))

        #escalon
        escalon_label = QLabel("Escalón N°",dlg)
        escalon_label.setFont(font_14b)
        escalon_label.setGeometry(QtCore.QRect(210, 20, 101, 16))
        num_escalon = QLabel("0",dlg) #necesita setText
        num_escalon.setFont(font_14b)
        num_escalon.setGeometry(QtCore.QRect(310, 20, 41, 16))

        #tematica
        tematica_label = QLabel("Temática:",dlg)
        tematica_label.setFont(font_14b)
        tematica_label.setGeometry(QtCore.QRect(70, 60, 91, 16))
        nombre_tematica = QLabel("Temática",dlg) #necesita un setText
        nombre_tematica.setFont(font_14)
        nombre_tematica.setGeometry(QtCore.QRect(160, 60, 101, 16))

        #Seleccionar
        seleccione = QLabel("Seleccione respuesta",dlg)
        seleccione.setFont(font_11b)
        seleccione.setGeometry(QtCore.QRect(210, 170, 151, 51))

        #Respuestas
        respuesta_a = QLabel("Respuesta a", dlg)
        respuesta_a.setGeometry(QtCore.QRect(70, 230, 231, 81))
        respuesta_a.setFont(font_11)
        respuesta_a.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_a.setWordWrap(True)

        respuesta_b = QLabel("Respuesta b", dlg)
        respuesta_b.setGeometry(QtCore.QRect(70, 340, 231, 81))
        respuesta_b.setFont(font_11)
        respuesta_b.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_b.setWordWrap(True)

        respuesta_c = QLabel("Respuesta c", dlg)
        respuesta_c.setGeometry(QtCore.QRect(360, 230, 231, 81))
        respuesta_c.setFont(font_11)
        respuesta_c.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_c.setWordWrap(True)

        respuesta_d = QLabel("Respuesta d", dlg)
        respuesta_d.setGeometry(QtCore.QRect(360, 340, 231, 81))
        respuesta_d.setFont(font_11)
        respuesta_d.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        respuesta_d.setWordWrap(True)

        #opciones
        opcion_a = QPushButton("A", dlg)
        opcion_a.setGeometry(QtCore.QRect(20, 230, 41, 31))
        opcion_b = QPushButton("B",dlg)
        opcion_b.setGeometry(QtCore.QRect(20, 340, 41, 31))
        opcion_c = QPushButton("C",dlg)
        opcion_c.setGeometry(QtCore.QRect(310, 230, 41, 31))
        opcion_d = QPushButton("D",dlg)
        opcion_d.setGeometry(QtCore.QRect(310, 340, 41, 31))

        dlg.exec()


    def setRespuestaCorrecta(self, boton, ):
        pass



#para controlador nuevo jugador
# self.muestra_imagenes()

# lista = ["img1", "img2", "img3"]

# qlabel = "img"


# img = 0

# button_avanzar.clicked

# img += 1
# qlabel = lista[img] 

# button_Retroceder.clicked
# img -= 1
# qlabel = lista[img]
    



