from modelo.Config_BD import Database
from Jugador import Jugador

class DAOjugador:
    def _init_(self):
        self.db = Database()

    def agregar_jugador(self, nombre_usuario, puntaje, activo):
        conn = self.db.get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO jugador (nombre_usuario, puntaje, activo)
                    VALUES (%s, %s, %s) RETURNING id_usuario;
                """, (nombre_usuario, puntaje, activo))
                conn.commit()
                jugador_id = cur.fetchone()[0]
                return jugador_id
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            self.db.put_conn(conn)

    def obtener_jugador(self, id_usuario):
        conn = self.db.get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM jugador WHERE id_usuario = %s;", (id_usuario,))
                row = cur.fetchone()
                if row:
                    return Jugador(*row)
                return None
        except Exception as e:
            raise e
        finally:
            self.db.put_conn(conn)

    def actualizar_jugador(self, id_usuario, nombre_usuario=None, puntaje=None, activo=None):
        conn = self.db.get_conn()
        try:
            with conn.cursor() as cur:
                if nombre_usuario:
                    cur.execute("UPDATE jugador SET nombre_usuario = %s WHERE id_usuario = %s;", (nombre_usuario, id_usuario))
                if puntaje is not None:
                    cur.execute("UPDATE jugador SET puntaje = %s WHERE id_usuario = %s;", (puntaje, id_usuario))
                if activo is not None:
                    cur.execute("UPDATE jugador SET activo = %s WHERE id_usuario = %s;", (activo, id_usuario))
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            self.db.put_conn(conn)

    def eliminar_jugador(self, id_usuario):
        conn = self.db.get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM jugador WHERE id_usuario = %s;", (id_usuario,))
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            self.db.put_conn(conn)