import mysql.connector

#Creando un conector
mydb = mysql.connector.Connect(
  host="localhost",
  user="root",
  password='123123321',
    
)
#Creando un cursor
miCursor = mydb.cursor() 

#Creando una tabla
miCursor.execute('CREATE DATABASE prueba')
miCursor.execute('USE prueba')
miCursor.execute("CREATE TABLE Empleados (nombre VARCHAR(100), edad INT(10), email VARCHAR(30))")
#Agregar una columna a la tabla
miCursor.execute("ALTER TABLE Empleados ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#Insetar registros
sql=("INSERT INTO Empleados (nombre,edad,email) VALUES(%s,%s,%s)")
Valores=("Emilio Antonio",20,"al03002006@tecmilenio.mx")
miCursor.execute(sql,Valores)
mydb.commit()

#Consultar la tabla
miCursor.execute("SELECT * FROM Empleados")
consulta=miCursor.fetchall()
mydb.commit()

#Insertar mas registros
sql=("INSERT INTO Empleados (nombre,edad,email) VALUES(%s,%s,%s)")
valores=[
  ('Pedro',35, 'Lowstreet@hotmail.com'),
  ('Amy',22, 'Apple34@hotmail.com'),
  ('Hannah',26, 'Mountain@sunshine.com'),
  ('Michael',31, 'Valley22@sunshine.com')
  ]
miCursor.executemany(sql,valores)
mydb.commit()

#Eliminar registro
sql=("DELETE FROM Empleados WHERE id=2")
miCursor.execute(sql)
mydb.commit()

#Modificar registro
miCursor.execute("UPDATE Empleados SET nombre='Miguel' WHERE nombre='Michael'")
mydb.commit()

#Cerrar la conexión
miCursor.close()
mydb.close()