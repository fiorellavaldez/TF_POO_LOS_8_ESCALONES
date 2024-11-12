from .JugadorDAO import JugadorDAO

class Jugador:
    def __init__(self, id_jugador, nombre_jugador, puntaje, estado_jugador):
        self.__jugadordao = JugadorDAO()
        self.__id_jugador = id_jugador
        self.__nombre_jugador = nombre_jugador
        self.__puntaje = puntaje
        self.__estado_jugador = estado_jugador
    

    def get_all_jugadores(self):
        return self.__jugadordao.get_all_jugadores()


    def get_jugador(self, id_jugador):
        return self.__jugadordao.get_jugador(id_jugador)


    def agregar_jugador(self, jugador):
        return self.__jugadordao.agregar_jugador(jugador)


    def actualizar_jugador(self, jugador):
        return self.__jugadordao.actualizar_jugador(jugador)


    def borrar_jugador(self, id_jugador):
        return self.__jugadordao.borrar_jugador(id_jugador)
    
    #GETTERS Y SETTERS
    def get_id_jugador (self):
        return self.__id_jugador
    def get_nombre_jugador(self):
        return self.__nombre_jugador
    def get_puntaje(self):
        return self.__puntaje
    def get_estado_jugador(self):
        return self.__estado_jugador
    def set_id_jugador (self, id_jugador):
        self.__id_jugador = id_jugador
    def set_nombre_jugador (self, nombre_jugador):
        self.__nombre_jugador = nombre_jugador
    def set_puntaje (self,puntaje):
        self.__puntaje = puntaje
    def set_estado_jugador (self, estado_jugador):
        self.__estado_jugador = estado_jugador
