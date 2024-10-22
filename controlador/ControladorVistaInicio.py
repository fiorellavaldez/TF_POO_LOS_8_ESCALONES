from controlador.ControladorConfiguracion import ControladorConfiguracion
from vista.VistaInicio import Ui_MainWindow

class ControladorVistaInicio:
    def __init__(self):
        self.__vista = Ui_MainWindow()
        self.__vista.get_button_configuracion().clicked.connect(self.__configuracion) #Clickear el boton (Es un evento) ?

    def __configuracion(self):
        return ControladorConfiguracion(self)