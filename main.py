from Controlador.ControladorInicio import ControladorInicio
from PyQt6 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controlador = ControladorInicio()
    sys.exit(app.exec()) #hola

