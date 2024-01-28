# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:49:58 2023
@author: vicen
"""
 # -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:47:42 2023
@author: Maximus Cristian Hernandez Garcia
 AL03007777
"""
import pandas as pd
import mysql.connector
# Cargar el dataset original
datos = pd.read_csv('99DA8014-0CA7-4BBD-977C-3E4D2E8D22F8_Tarifas.csv')
print (datos.head())
datos['fecha_inicio'] = pd.to_datetime(datos['fecha_inicio'],
format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
datos['fecha_fin'] = pd.to_datetime(datos['fecha_fin'],
format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
# Establecer la conexión a la base de datos MySQL
mydb = mysql.connector.connect(
 host = "localhost",
 user = "root",
 password = 'Revsbl14donut@',
 database="Tarifas" # Nombre de la base de datos creada en MySQL Workbench
)
cursor = mydb.cursor()
# Crear la tabla en la base de datos (si no existe) con la estructura correcta
create_table_query = """
CREATE TABLE IF NOT EXISTS tarifas (
 zona VARCHAR(100),
 capacidad_base_firme FLOAT,
 uso_base_firme FLOAT,
 capacidad_base_temporal FLOAT,
 uso_base_temporal FLOAT,
 maxima_base_interrumpible FLOAT,
 minima_base_interrumpible FLOAT,
 volumetrica FLOAT,
 fecha_inicio DATE,
 fecha_fin DATE
);
"""
cursor.execute(create_table_query)
# Insertar los datos del DataFrame en la tabla de la base de datos
for _, row in datos.iterrows():
 sql = """
 INSERT INTO tarifas (zona, capacidad_base_firme, uso_base_firme,
capacidad_base_temporal, uso_base_temporal,
 maxima_base_interrumpible, minima_base_interrumpible, volumetrica,
fecha_inicio, fecha_fin)
 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
 """
 cursor.execute(sql, (row['zona'], row['capacidad_base_firme'],
row['uso_base_firme'], row['capacidad_base_temporal'],
 row['uso_base_temporal'], row['maxima_base_interrumpible'],
row['minima_base_interrumpible'],
 row['volumetrica'], row['fecha_inicio'], row['fecha_fin']))
import matplotlib.pyplot as plt
# Consultar los datos necesarios para las visualizaciones
cursor.execute('SELECT fecha_inicio, capacidad_base_firme, uso_base_firme,
capacidad_base_temporal, uso_base_temporal FROM tarifas')
resultados = cursor.fetchall()
# Crear un DataFrame con los resultados de la consulta
df = pd.DataFrame(resultados, columns=['fecha_inicio', 'capacidad_base_firme',
'uso_base_firme', 'capacidad_base_temporal', 'uso_base_temporal'])
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])
# Visualización g) Gráfico de línea para la variación de las tarifas contra el
tiempo para los dos años
plt.figure(figsize=(12, 6))
# Plotear las líneas y añadir etiquetas
plt.plot(df['fecha_inicio'], df['capacidad_base_firme'], label='Capacidad Base
Firme', marker='s')
plt.plot(df['fecha_inicio'], df['uso_base_firme'], label='Uso Base Firme',
marker='s')
plt.plot(df['fecha_inicio'], df['capacidad_base_temporal'], label='Capacidad Base
Temporal', marker='o')
plt.plot(df['fecha_inicio'], df['uso_base_temporal'], label='Uso Base Temporal',
marker='o')
# Configuración del título y etiquetas de los ejes
plt.title('Variación de Tarifas contra el Tiempo')
plt.xlabel('Fecha de Inicio')
plt.ylabel('Tarifas')
# Mostrar la leyenda
plt.legend(['Capacidad Base Firme', 'Uso Base Firme', 'Capacidad Base Temporal',
'Uso Base Temporal'])
#Cuadrícula de fondo
plt.grid(True)
# Mostrar el gráfico
plt.show()
# Visualización h) Gráfico de barras para máximos y mínimos de las tarifas por mes
de cada uno de los dos años
df['mes'] = df['fecha_inicio'].dt.month
# Agrupar por mes y calcular los máximos y mínimos
maximos_por_mes = df.groupby('mes').max()
minimos_por_mes = df.groupby('mes').min()
plt.figure(figsize=(12, 6))
bar_width = 0.35
# Crear barras para los máximos y mínimos, ajustando las posiciones
plt.bar(maximos_por_mes.index - bar_width / 2,
maximos_por_mes['capacidad_base_firme'], bar_width, label='Máximo Base Firme')
plt.bar(minimos_por_mes.index + bar_width / 2,
minimos_por_mes['capacidad_base_firme'], bar_width, label='Mínimo Base Firme')
# Configuracion del título y etiquetas de ejes
plt.title('Máximos y Mínimos de Tarifas por Mes')
plt.xlabel('Mes')
plt.ylabel('Tarifas')
# Mostrar la leyenda
plt.legend()
#Cuadrícula de fondo
plt.grid(True)
# Mostrar el gráfico
plt.show()
# Hacer commit para guardar los cambios
mydb.commit()
# Consultar los registros insertados
cursor.execute('SELECT * FROM tarifas')
consulta = cursor.fetchall()
for fila in consulta:
print(fila)
# Cerrar la conexión
cursor.close()
mydb.close()