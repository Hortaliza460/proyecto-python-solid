import sqlite3


class Conexion:
    def __init__(self):
        self.ruta = "database/ventas.db"

    def conectar(self):
        return sqlite3.connect(self.ruta)

    def crear_tablas(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL
            )
        """)
        conexion.commit()
        conexion.close()
