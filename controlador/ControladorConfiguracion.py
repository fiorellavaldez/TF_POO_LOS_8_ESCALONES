from vista.VistaConfiguracion import Ui_MainWindow


class ControladorConfiguracion:
    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.__vista = Ui_MainWindow()
        self.__vista.get_button_configuracion().clicked.connect(self.__volver_menu)

            

    def __volver_menu(self):
        return self.__controlador_anterior #Es así?