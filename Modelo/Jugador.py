class Jugador():
    def __init__ (self, nombre, avatar):

        #Constructor para inicializar un jugador.
        #-parametro nombre: str, nombre del jugador
        #-parametro avatar: str, avatar del jugador (puede ser una cadena con la ruta de la imagen o el nombre del avatar)

        self.__nombre = nombre  # Nombre del jugador
        self.__avatar = avatar  # Avatar del jugador
        self.__ronda1 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__ronda2 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__escalon_actual = 1  # Escalón inicial

    def avanzar_escalon(self):
        # Método para avanzar al siguiente escalón
        self.__escalon_actual += 1