from vista.VistaIngresarNombres import Ui_MainWindow
from PyQt6 import QtWidgets

class ControladorIngresarNombres:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la configuración
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.__vista.get_button_atras().clicked.connect(self.__volver_menu)

    def __volver_menu(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()
