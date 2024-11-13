import psycopg2
from .bd import Database
import hashlib
import random

class TemasDAO:
    def __init__(self):
        self.__bd = Database()

    def get_all_temas(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * FROM temas")
            return cursor.fetchall()

    def get_tema(self, id_tema):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT id_tema, nombre_tema FROM temas WHERE id_tema = %s", (id_tema,))
            return cursor.fetchone()

    def agregar_tema(self, tema):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                "INSERT INTO temas (id_tema, nombre_tema) VALUES (%s, %s)",
                (tema.get_id_tema(), tema.get_nombre_tema())
            )
            indice_tema = cursor.execute ("SELECT MAX(id_tema) FROM temas ")
            tema.set_id_tema(int(indice_tema)) #esto lo que hace es incrementar el indice porque los id son tipo serial
            self.__bd.commit()
            

    def actualizar_tema(self, tema):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                "UPDATE temas SET nombre_tema = %s WHERE id_tema = %s",
                (tema.get_nombre_tema(), tema.get_id_tema())
            )
            self.__bd.commit()

    def temas_partida (self): #Agarramos la informacion de tablas de teams y seleccionamos 8 temas al azar y los guardamos en una lista
        temas = self.get_all_temas()
        lista_temas_partida = []
        random.shuffle(temas)
        for i in range (0,7):
            lista_temas_partida.append(temas.pop())
        return lista_temas_partida    
    
    def devolver_preg_ronda (self, id_tema): #posible id tema
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'Ronda' and id_tema_pregunta = %s", (id_tema,))
            return cursor.fetchall()
        
    def devolver_pregunta_desempate (self, id_tema): #posible id tema
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'Desempate' and id_tema_pregunta = %s", (id_tema,))
            return cursor.fetchall()

    #def borrar_tema(self, id_tema):
       # with self.connection.cursor() as cursor:
        #    cursor.execute("DELETE FROM temas WHERE id_tema = %s", (id_tema,))
         #   self.connection.commit() COMO NO SE TIENE QUE BORRAR INFO Y TEMAS NO TIENE UN ESTADO PARA PONERLO EN FALSO ENTONCES EL METODO BORRAR CREO QUE NO VA EN TEMA
