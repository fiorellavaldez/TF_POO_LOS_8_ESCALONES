import psycopg2
from .bd import Database
import hashlib

class JugadorDAO:
    def __init__(self):
        self.__bd = Database()
    

    def get_all_jugadores(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT nombre_jugador, puntaje FROM jugador")
            return cursor.fetchall()

    def get_jugador(self, id_jugador):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT nombre_jugador, puntaje FROM jugador WHERE id_jugador = %s", (id_jugador,))
            return cursor.fetchone()

    def agregar_jugador(self, id_jugador, nombre_jugador, puntaje , estado_jugador):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO jugador (id_jugador, nombre_jugador, puntaje , estado_jugador) 
                VALUES (%s, %s, %s, %s)""",
                (id_jugador, nombre_jugador, puntaje , estado_jugador)
            )
            self.connection.commit()

    def actualizar_jugador(self, id_jugador, nombre_jugador, puntaje):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """UPDATE jugador SET nombre_jugador = %s, puntaje = %s 
                WHERE id_jugador = %s""",
                (nombre_jugador, puntaje, id_jugador)
            )
            self.connection.commit()

    def borrar_jugador(self, id_jugador):
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE jugador SET estado_jugador FALSE WHERE id_jugador = %s", (id_jugador,))
            self.connection.commit()