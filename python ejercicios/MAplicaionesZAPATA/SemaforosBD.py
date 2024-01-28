import sqlite3

conn1 = sqlite3.connect('Semaforos_Calles.db')
cursor1 = conn1.cursor()

cursor1.execute('''
    CREATE TABLE IF NOT EXISTS Semaforos_Calles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre_del_lugar TEXT,
        transicion_de_los_colores INTEGER CHECK (transicion_de_los_colores >= 30 AND transicion_de_los_colores <= 120)
    )
''')

conn1.commit()
conn1.close()
conn2 = sqlite3.connect('personas.db')
cursor2 = conn2.cursor()

cursor2.execute('''
    CREATE TABLE IF NOT EXISTS personas (
        IDpersona INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        telefono TEXT
    )
''')
conn2.commit()
conn2.close()

conn3 = sqlite3.connect('usuarios.db')
cursor3 = conn3.cursor()

cursor3.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id_Semaforo_Calles INTEGER,
        IDpersona INTEGER,
        locacion TEXT,
        tiempo_del_trafico TEXT,
        FOREIGN KEY (id_Semaforo_Calles) REFERENCES Semaforos_Calles(id),
        FOREIGN KEY (IDpersona) REFERENCES personas(IDpersona)
    )
''')

conn3.commit()
conn3.close()