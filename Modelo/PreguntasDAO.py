import psycopg2
from .bd import Database
import hashlib

class PreguntasDAO:
    def __init__(self):
        self.__bd = Database()
    

    def get_all_preguntas(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM preguntas")
            return cursor.fetchall()

    def get_pregunta(self, id_pregunta):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM preguntas WHERE id_pregunta = %s", (id_pregunta,))
            return cursor.fetchone()

    def agregar_pregunta(self, id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO preguntas (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta)
            )
            self.connection.commit()

    def actualizar_pregunta(self, id_pregunta, enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """UPDATE preguntas SET enunciado_pregunta = %s, rta_a = %s, rta_b = %s, rta_c = %s, rta_d = %s, rta_correcta = %s, tipo_pregunta = %s, estado_pregunta = %s 
                WHERE id_pregunta = %s""",
                (enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_pregunta)
            )
            self.connection.commit()

    def borrar_pregunta(self, id_pregunta):
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE preguntas SET estado_pregunta FALSE WHERE id_pregunta = %s", (id_pregunta,))
            self.connection.commit()
