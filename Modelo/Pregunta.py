from .PreguntasDAO import PreguntasDAO

class Pregunta:
    
    def __init__(self):
        self.__pregdao = PreguntasDAO()
    
    def get_all_preguntas(self):
        return self.__pregdao.get_all_preguntas()

    def get_pregunta_by_id(self, id_pregunta):
        return self.__pregdao.get_pregunta(id_pregunta)

    def agregar_pregunta(self, id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunt):
        return self.__pregdao(self, id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunt)

    def actualizar_pregunta(self, id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunt):
        return self.__pregdao(self, id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunt)

    def borrar_pregunta(self, id_pregunta):
        return self.__pregdao.borrar_preguntas(id_pregunta)
