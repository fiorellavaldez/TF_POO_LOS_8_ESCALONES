from Vista.VistaConfiguracion import Ui_MainWindow
from Controlador.ControladorTemaNuevo import ControladorTemaNuevo
from PyQt6 import QtWidgets

class ControladorConfiguracion:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la configuración
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)
        self.__vista.get_button_tema_nuevo().clicked.connect(self.__tema_nuevo)

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior
        #hide() permite volver a abrir la misma ventana (.show()) sin perder su estado o tener que volver a inicializarla
        #close() cierra la ventana y destruye el objeto asociado, no se le puede hacer .show(), usar cuando ya no se necesita la ventana y se quiere liberar recursos
        # by ChatGpt

    def __tema_nuevo(self):
        self.MainWindow.hide()
        self.controlador_tema_nuevo = ControladorTemaNuevo(self)
    
