from vista.VistaJuego import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

class ControladorVistaJuego:

    def __init__(self, controlador_anterior):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__atras)
        self.__vista.get_button_pregunta().clicked.connect(self.__obtener_pregunta)

    def __atras(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def __obtener_pregunta(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("¡Aviso!")
        dlg.setText("Este es un dialog que sirve para mostrar un aviso.")
       # dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")