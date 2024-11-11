from .TemasDAO import TemasDAO

class Temas:
    
    def __init__(self):
        self.__temasdao = TemasDAO()


    def get_all_temas(self):
        return self.__temasdao.get_all_temas()

    def get_tema(self, id_tema):
        return self.__temasdao.get_tema(id_tema)

    def agregar_tema(self, id_tema, nombre_tema):
        return self.__temasdao.agregar_tema(id_tema,nombre_tema)


    def actualizar_tema(self, id_tema, nombre_tema):
        return self.__temasdao.actualizar_temas(id_tema, nombre_tema)


    def borrar_tema(self, id_tema):
        return self.__temasdao.borrar_tema(id_tema)

