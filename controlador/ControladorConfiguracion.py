from vista.VistaConfiguracion import Ui_MainWindow
from controlador.ControladorTemaNuevo import ControladorTemaNuevo
from controlador.ControladorModificarTemas import ControladorModificarTemas
from controlador.ControladorVistaConfiguracionModificarPreguntasDesempate import ControladorVistaConfiguracionModificarPreguntasDeDesempate
from controlador.ControladorVistaConfiguracionModificarPreguntasRonda import ControladorVistaConfiguracionModificarPreguntasRonda

from PyQt6 import QtWidgets

class ControladorConfiguracion:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la configuración
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_modificar_preguntas_ronda().clicked.connect(self.__modificar_preguntas_ronda)
        self.__vista.get_button_modificar_preguntas_desempate().clicked.connect(self.__modificar_preguntas_desempate)
        self.__vista.get_button_modificar_temas().clicked.connect(self.__modificar_temas)
        self.__vista.get_button_tema_nuevo().clicked.connect(self.__tema_nuevo)
        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)

    def __modificar_preguntas_ronda(self):
        self.MainWindow.hide()
        self.controlador_modificar_preguntas_ronda = ControladorVistaConfiguracionModificarPreguntasRonda(self)

    def __modificar_preguntas_desempate(self):
        self.MainWindow.hide()
        self.controlador_modificar_preguntas_desempate = ControladorVistaConfiguracionModificarPreguntasDeDesempate(self)

    def __modificar_temas(self):
        self.MainWindow.hide()
        self.controlador_modificar_temas = ControladorModificarTemas(self)

    def __tema_nuevo(self):
        self.MainWindow.hide()
        self.controlador_tema_nuevo = ControladorTemaNuevo(self)

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()  # Muestra la ventana anterior
        #hide() permite volver a abrir la misma ventana (.show()) sin perder su estado o tener que volver a inicializarla
        #close() cierra la ventana y destruye el objeto asociado, no se le puede hacer .show(), usar cuando ya no se necesita la ventana y se quiere liberar recursos