from .TemasDAO import TemasDAO

class Temas:
    
    def __init__(self, id_tema, nombre_tema):
        self.__temasdao = TemasDAO()
        self.__id_tema = id_tema
        self.__nombre_tema = nombre_tema


    def get_all_temas(self):
        return self.__temasdao.get_all_temas()

    def get_tema(self, id_tema):
        return self.__temasdao.get_tema(id_tema)

    def agregar_tema(self, tema):
        return self.__temasdao.agregar_tema(tema)


    def actualizar_tema(self, tema):
        return self.__temasdao.actualizar_tema(tema)


    #def borrar_tema(self, id_tema):
        #return self.__temasdao.borrar_tema(id_tema)

#GETTERS Y SETTER
    def get_id_tema (self):
        return self.__id_tema
    def get_nombre_tema (self):
        return self.__nombre_tema
    def set_id_tema (self, id_tema):
        self.__id_tema = id_tema
    def set_nombre_tema (self,nombre_tema):
        self.__nombre_tema = nombre_tema




