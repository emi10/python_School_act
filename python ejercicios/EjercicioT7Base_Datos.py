'''
Primer programa de base de datos 
Emilio Antonio Gallegos Bedolla
28/09/2023
Usando la libreria de sqlite

'''
import sqlite3


# Establecer conexioón
conexion = sqlite3.connect("agenda.db")
#Creacion de un cursor 
cursor = conexion.cursor()

#Crear una tabla 
"""
conexion.execute('''CREATE TABLE agenda
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT NOT NULL,
                 direccion TEXT NOT NULL,
                 telefono TEXT NOT NULL);''')

"""
"""
#Agregar registros 
valores=("Emilio Antonio Gallegos Bedolla", "Francisco trujillo 86029", "9372266070") #Tupla
sql='''INSERT INTO agenda(nombre, direccion, telefono) VALUES(?,?,?)'''
cursor.execute(sql,valores)
conexion.commit()

#Consulta de la base de datos 
cursor.execute("SELECT * FROM agenda")
contactos = cursor.fetchall()
for w in contactos:
    print(w)
""" 

#Agregar varios valores 
"""
valores=[("Antonio Gallegos", "Trujillo Francisco 86029", "88564376"),("Gerardor gutierrez Gallegos", "Trujillo Francisco", "7653470977"),("Pedrito sola", "Av gutierrez 86029", "6634764234")]
sql ='''INSERT INTO agenda(nombre, direccion, telefono) VALUES(?,?,?)'''
cursor.executemany(sql, valores)
conexion.commit()
"""

# ELIMINAR REGISTROS    
"""
sql = '''DELETE FROM agenda WHERE id=?'''
valor = (1,)
cursor.execute(sql,valor)
conexion.commit ()
"""

#Actualizar resgistros

sql = '''UPDATE agenda SET nombre = ? WHERE id = ?'''
valores = ("Josue",3)
cursor.execute(sql,valores)
conexion.commit ()

conexion.close()
