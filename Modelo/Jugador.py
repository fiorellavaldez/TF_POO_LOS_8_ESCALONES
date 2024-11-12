from .JugadorDAO import JugadorDAO

class Jugador:
    def __init__(self, id_jugador, nombre_jugador, imagen, ronda1, ronda2, escalon_actual):
        #self.__jugadordao = JugadorDAO()
        #self.__id_jugador = id_jugador
        self.__nombre_jugador = nombre_jugador
        self.__imagen = imagen
        #self.__puntaje = puntaje
        #self.__estado_jugador = estado_jugador
        self.__ronda1 = ronda1
        self.__ronda2 = ronda2
        self.__escalon_actual = escalon_actual
    

    # def get_all_jugadores(self):
    #     return self.__jugadordao.get_all_jugadores()


    # def get_jugador(self, id_jugador):
    #     return self.__jugadordao.get_jugador(id_jugador)


    # def agregar_jugador(self, jugador):
    #     return self.__jugadordao.agregar_jugador(jugador)


    # def actualizar_jugador(self, jugador):
    #     return self.__jugadordao.actualizar_jugador(jugador)


    # def borrar_jugador(self, id_jugador):
    #     return self.__jugadordao.borrar_jugador(id_jugador)

    #GETTERS Y SETTERS
    def get_nombre_jugador(self):
        return self.__nombre_jugador

    def get_escalon_actual(self):
        return self.__escalon_actual

    def get_imagen(self):
        return self.__imagen

    def get_ronda1(self):
        return self.__ronda1

    def get_ronda2(self):
        return self.__ronda2

    def set_nombre_jugador (self, nombre_jugador):
        self.__nombre_jugador = nombre_jugador