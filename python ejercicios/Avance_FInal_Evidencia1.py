'''
Avance Final evidencia 1 Big Data
Emilio Antonio Gallegos Bedolla
22/10/2023

'''
import pandas as pd
import mysql.connector


Datos = pd.read_csv('Tarifas por zonas 2016-2017.csv')

# Muestreo de datos

print (Datos.info())
print (Datos.describe())
print (Datos.head())

#Comando para eliminar valores nulos
Datos = Datos.fillna(0)

# se borran los valores de las filas que no son necesarias 
Datos.drop(["zona", "maxima_base_interrumpible", "minima_base_interrumpible", "volumetrica", "fecha_inicio","fecha_fin"],axis=1,inplace=True)



#Creando un conector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='123123321',
    
)
# Se crea un cursor con el cual se va a trabajar 
miCursor = mydb.cursor() 

# Creación de la tabla
miCursor.execute('CREATE DATABASE UsoBases')
miCursor.execute('USE UsoBases')
miCursor.execute("CREATE TABLE RegistroBase (capacidad_base_firme FLOAT, uso_base_firme FLOAT, capacidad_base_temporal FLOAT, uso_base_temporal FLOAT)")
#Agregar una columna a la tabla
miCursor.execute("ALTER TABLE RegistroBase ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#Transferir el data frame a la data base 
for x, row in Datos.iterrows():
   sql = 'INSERT INTO RegistroBase (capacidad_base_firme, uso_base_firme, capacidad_base_temporal, uso_base_temporal) VALUES (%s, %s, %s, %s)'
   miCursor.execute(sql, tuple(row))
   mydb.commit()

    
#Consultar los registros 
miCursor.execute(' SELECT * FROM RegistroBase')
consulta = miCursor.fetchall()
for x in consulta:
    print(x)

