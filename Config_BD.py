import psycopg2
from psycopg2 import pool

class Database:
    __instance = {}

    def _new_(cls):
        if cls.__instance is None:
            cls._instance = object.new_(cls)
            cls.__instance.pool = psycopg2.pool.SimpleConnectionPool(1, 20,
                dbname="8_escalones",
                user="public",
                password="pokemon",
                host="localhost",
                port="5432"
            )
        return cls.__instance

    def get_conn(self):
        return self.pool.getconn()

    def put_conn(self, conn):
        self.pool.putconn(conn)