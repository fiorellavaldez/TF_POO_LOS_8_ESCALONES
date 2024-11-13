import psycopg2
from .bd import Database
import hashlib

class JugadorDAO:
    def __init__(self):
        self.__bd = Database()
    

    def get_all_jugadores(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT nombre_jugador, puntaje FROM jugador")
            return cursor.fetchall()

    def get_jugador(self, id_jugador):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT nombre_jugador, puntaje FROM jugador WHERE id_jugador = %s", (id_jugador,))
            return cursor.fetchone()

    def agregar_jugador(self, jugador):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """INSERT INTO jugador (id_jugador, nombre_jugador, puntaje , estado_jugador) 
                VALUES (%s, %s, %s, %s)""",
                (jugador.get_id_jugador(), jugador.get_nombre_jugador(), jugador.get_puntaje() , jugador.get_estado_jugador())
            )
            indice_jugador = cursor.execute ("SELECT MAX(id_jugador) FROM jugador ")
            jugador.set_id_jugador (int(indice_jugador)) #esto lo que hace es incrementar el indice porque los id son tipo serial
            self.__bd.commit()


    def actualizar_jugador(self, jugador):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """UPDATE jugador SET nombre_jugador = %s, puntaje = %s 
                WHERE id_jugador = %s""",
                (jugador.get_nombre_jugador(), jugador.get_puntaje(), jugador.get_id_jugador())
            )
            self.__bd.commit()

    def borrar_jugador(self, id_jugador):
        with self.__bd.cursor() as cursor:
            cursor.execute("UPDATE jugador SET estado_jugador FALSE WHERE id_jugador = %s", (id_jugador,))
            self.__bd.commit()
