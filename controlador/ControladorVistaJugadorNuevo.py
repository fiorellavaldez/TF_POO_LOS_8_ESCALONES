from vista.VistaJugadorNuevo import Ui_MainWindow
from PyQt6 import QtWidgets
from modelo.Jugador import Jugador

class ControladorVistaJugadorNuevo:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        self.__vista.get_button_aceptar().clicked.connect(self.__agregar_jugador_bd_)
        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)
        
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
        
    def __agregar_jugador_bd_(self):
        try:
            nombre_jugador=self.__vista.get_entrada_texto()
            
            if None in nombre_jugador or '' in nombre_jugador:
                raise ValueError
            else:
                jugador_nuevo=Jugador()
                jugador_nuevo.agregar_jugador(nombre_jugador)
                self.__vista.notifico_insercion(nombre_jugador)
                self.MainWindow.close()
        except:
                self.__vista.imprimo_alerta()