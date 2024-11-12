from .JugadorDAO import JugadorDAO

class Jugador:
    def __init__(self):
        self.__jugadordao = JugadorDAO()
    

    def get_all_jugadores(self):
        return self.__jugadordao.get_all_jugadores()


    def get_jugador(self, id_jugador):
        return self.__jugadordao.get_jugador(id_jugador)

    '''
    def agregar_jugador(self, id_jugador, nombre_jugador, puntaje , estado_jugador):
        return self.__jugadordao.agregar_jugador(id_jugador, nombre_jugador, puntaje , estado_jugador)
    '''
    #nos interesa agregar solo el nombre el ID ya es de tipo SERIAL no es neceario pasar como parametro
    def agregar_jugador(self, nombre_jugador,img_avatar):
        return self.__jugadordao.agregar_jugador( nombre_jugador,img_avatar)

    def actualizar_jugador(self, id_jugador, nombre_jugador, puntaje):
        return self.__jugadordao.actualizar_jugador(id_jugador, nombre_jugador, puntaje)


    def borrar_jugador(self, id_jugador):
        return self.__jugadordao.borrar_jugador(id_jugador)
