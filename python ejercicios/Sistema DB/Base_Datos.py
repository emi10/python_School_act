import os
import sqlite3

class BaseDatos:
    def __init__(self, nombreBaseDatos):
        self.nombreBaseDatos = nombreBaseDatos

    def crearBaseDatos(self):
        conexion = sqlite3.connect (self.nombreBaseDatos)

    def crearTabla (self):
        conexion = sqlite3.connect(self.nombreBaseDatos)
        conexion.execute('''CREATE TABLE productos 
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         nombre TEXT NOT NULL,
                         descripcion TEXT NOT NULL,
                         precio FLOAT NOT NULL,
                         stock INTEGER NOT NULL);''')
        conexion.close()

    def verificacionBD (self):
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
            return False