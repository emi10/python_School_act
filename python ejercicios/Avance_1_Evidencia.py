'''
Avance 1 evidencia 1 Big Data
Emilio Antonio Gallegos Bedolla
26/09/2023

'''

import pandas

data = pandas.read_csv("Tarifas por zonas 2016-2017.csv")

#analisis exploratorio basico 
print (data.info())
print (data.describe())
print (data.head())

'''
Avance 2 evidencia 1 Big Data
Emilio Antonio Gallegos Bedolla
12/10/2023

'''



pandas.crosstab(data ['zona'],data['uso_base_firme'])

#Funcion para el promedio de la tarifa de uso de base firme
data.groupby(['zona'])['uso_base_firme'].mean()

#crear otro grupo con año
data['fecha_inicio'] = pandas.to_datetime(data['fecha_inicio'])
data['Anio'] = data['fecha_inicio'].dt.year
data ['Mes'] = data ['fecha_inicio'].dt.month

data2=data.groupby(['zona', 'Anio'])['uso_base_firme'].mean()
data2 = data2.to_frame()
prom16 = data2.query('Anio == 2016')
prom17 = data2.query('Anio == 2016')

#Funciones para filtrar por año
print(prom16)
print(prom17)

#Tarifa máximas 
datamax = data.groupby(['zona', 'Anio'])['uso_base_firme'].max()
print(datamax)

datamax = datamax.to_frame()

max16 = datamax.query('Anio == 2016')
max17 = datamax.query('Anio == 2016')
print(max16)
print(max17)
