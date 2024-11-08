from vista.VistaSeleccionarJugadores import Ui_MainWindow
from PyQt6 import QtWidgets

class ControladorVistaSeleccionarJugadores:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        self.__vista.get_button_aceptar().clicked.connect(self.__aceptar)
        self.__vista.get_button_atras().clicked.connect(self.__volver_seleccion_de_jugadores)
        

    def __aceptar(self):
        self.MainWindow.close()
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show() 
        
        