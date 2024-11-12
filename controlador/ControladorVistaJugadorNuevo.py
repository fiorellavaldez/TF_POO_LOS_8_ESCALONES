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
        
        self.__vista.get_button_agregar_jugador().clicked.connect(self.__agregar_jugador_bd_)
        self.__vista.get_button_cancelar().clicked.connect(self.__volver_seleccion_de_jugadores)
        #self.__vista.get_boton_deslizador_derecha().clicked.connect(self.__mostrar_siguiente_imagen)
        #self.__vista.get_boton_deslizador_izquierda().clicked.connect(self.__mostrar_imagen_anterior)
        
    def __volver_seleccion_de_jugadores(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
        
    def __agregar_jugador_bd_(self):
        #Agrega un nuevo jugador y su avatar a la BD,Validandolos
        try:
            nombre_jugador=self.__vista.get_entrada_texto()
            
            if not nombre_jugador:
                raise ValueError("El nombre del jugador esta vacio")
            else:
                jugador_nuevo=Jugador()
                jugador_nuevo.agregar_jugador(nombre_jugador)
                self.__vista.notifico_insercion(nombre_jugador)
                self.MainWindow.close()
        except:
                self.__vista.imprimo_alerta()
    '''            
    def __mostrar_siguiente_imagen(self):
        pass
    
    
    def __mostrar_imagen_anterior(self):
        pass
        
    '''
        
    