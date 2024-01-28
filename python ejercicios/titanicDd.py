'''
Actividad 7 Big Data
Emilio Antonio Gallegos Bedolla
12/10/2023
'''
import pandas as pd
import mysql.connector

datos= pd.read_csv('titanic.csv')



print(datos.head())
print(datos.info())

# ver y sumar valores nulos
print (datos.isnull().sum())

#Eliminar valores nulos
datos = datos.fillna(0)

# Eliminar columnas

datos.drop(["PassengerId","Survived", "Pclass", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"],axis=1,inplace=True) # si axis tiene uno es para columnas y 0 es para filas

# Eliminar filas 
datos.drop(range(102,890),axis=0,inplace=True)

print(datos.info())

#conexion a my Mysql
mydb = mysql.connector.Connect(
  host="localhost",
  user="root",
  password='123123321',

)

#Creando un cursor
cursor = mydb.cursor()
"""
# Crear BASE DE DATOS 
cursor.execute('CREATE DATABASE Titanic')
"""
cursor.execute('USE Titanic')
"""
#Crear las tablas
cursor.execute('CREATE TABLE Pasajeros (Nombre VARCHAR(100), Sexo VARCHAR (10), Edad INT(10))')
"""


"""
#Transferir el data frame a la data base 
for x, row in datos.iterrows():
    sql = ('INSERT INTO Pasajeros VALUES (%s,%s,%s)')
    cursor.execute(sql,tuple(row))
    mydb.commit()
"""

#Consultar los registros 
cursor.execute(' SELECT * FROM pasajeros')
consulta = cursor.fetchall()
for x in consulta:
    print(x)


#Realizar otra tabla
# Realizar la preparación del dataframe
#usar la mism sb, solo agregar otra tabla 
#adjuntar pantallas de evidencia y ejecución