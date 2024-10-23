from Controlador.ControladorConfiguracion import ControladorConfiguracion
from Controlador.ControladorIngresarNombres import ControladorIngresarNombres
from Vista.VistaInicio import Ui_MainWindow
from PyQt6 import QtWidgets

class ControladorInicio:

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_configuracion().clicked.connect(self.__configuracion) #Clickear el boton (Es un evento) ?
        self.__vista.get_button_nueva_partida().clicked.connect(self.__ingresar_nombres)
        self.__vista.get_button_salir().clicked.connect(self.__salir)

    def __configuracion(self):
        self.MainWindow.hide()
        self.controlador_configuracion = ControladorConfiguracion(self)

    def __ingresar_nombres(self):
        self.MainWindow.hide()
        self.controlador_ingresar_nombres = ControladorIngresarNombres(self)
    
    def __salir(self):
        self.MainWindow.close() #si es la última ventana abierta y hacemos .close(), se cierra el programa y termina la ejecución del bucle de Qt (que está en el main)