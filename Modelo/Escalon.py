class Escalon:
    def __init__(self, tema):
        self.__tema = tema
        self.__jugadores = []

    def get_tema(self):
        return self.__tema

    def preguntar_jugador(self):
        for i in self.__jugadores:
            