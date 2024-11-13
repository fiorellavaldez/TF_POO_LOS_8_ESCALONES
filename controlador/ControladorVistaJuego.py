from vista.VistaJuego import Ui_MainWindow
from vista.VistaPreguntaRonda import VistaPreguntaRonda
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
        vista_pregunta = VistaPreguntaRonda()
        vista_pregunta.exec()


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
    



