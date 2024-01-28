'''
Actividad 7 Big Data
Emilio Antonio Gallegos Bedolla
14/10/2023
Realizar los siguientes requerimientos 

- Realizar otra tabla
- Realizar la preparación del dataframe
- usar la mism sb, solo agregar otra tabla 
- adjuntar pantallas de evidencia y ejecución
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

datos.drop(["PassengerId","Name", "Embarked", "SibSp", "Parch", "Sex", "Fare", "Cabin", "Age"],axis=1,inplace=True) # si axis tiene uno es para columnas y 0 es para filas

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

cursor.execute('USE Titanic')
'''
#Crear la nueva tablas
cursor.execute('CREATE TABLE Embarcaciones (Survived INT(100), Pclass INT (10), Ticket VARCHAR (100))')
'''


'''
#Transferir el data frame a la data base 
for x, row in datos.iterrows():
    sql = ('INSERT INTO Embarcaciones VALUES (%s,%s,%s)')
    cursor.execute(sql,tuple(row))
    mydb.commit()
'''

#Consultar los registros 
cursor.execute(' SELECT * FROM Embarcaciones')
consulta = cursor.fetchall()
for x in consulta:
    print(x)


