from .PreguntasDAO import PreguntasDAO

class Pregunta:
    
    def __init__(self, id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema_pregunta):
        self.__pregdao = PreguntasDAO()
        self.__id_pregunta = id_pregunta
        self.__enunciado_pregunta = enunciado_pregunta
        self.__rta_a =  rta_a 
        self.__rta_b = rta_b
        self.__rta_c = rta_c
        self.__rta_d = rta_d
        self.__rta_correcta = rta_correcta
        self.__tipo_pregunta = tipo_pregunta
        self.__estado_pregunta = estado_pregunta
        self.__id_tema_pregunta = id_tema_pregunta
    
    def get_all_preguntas(self):
        return self.__pregdao.get_all_preguntas()

    def get_pregunta_by_id(self, id_pregunta):
        return self.__pregdao.get_pregunta(id_pregunta)

    def agregar_pregunta(self, pregunta):
        return self.__pregdao.agregar_pregunta(self, pregunta)

    def actualizar_pregunta(self, pregunta):
        return self.__pregdao(self, pregunta)

    def borrar_pregunta(self, id_pregunta):
        return self.__pregdao.borrar_pregunta(id_pregunta)
    
    #GETTERS Y SETTERS
    def set_id_pregunta (self, id_pregunta):
        self.__id_pregunta = id_pregunta
    def set_enunciado (self, enunciado_pregunta):
        self.__enunciado_pregunta = enunciado_pregunta

    def get_id_pregunta (self):
        return self.__id_pregunta    
    def get_enunciado (self):
        return self.__enunciado_pregunta   
    def get_rta_a (self):
        return self.__rta_a
    def get_rta_b (self):
        return self.__rta_b
    def get_rta_c (self):
        return self.__rta_c
    def get_rta_d (self):
        return self.__rta_d
    def get_rta_correcta (self):
        return self.__rta_correcta        
    def get_tipo_pregunta (self):
        return self.__tipo_pregunta
    def get_estado_pregunta (self):
        return self.__estado_pregunta
    def get_id_tema_pregunta (self):
        return self.__id_tema_pregunta
