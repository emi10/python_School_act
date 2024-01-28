#Emilio Antonio Gallegos Bedolla 
#Al03002006
#30 noviembre del 2023
#Evidencia final 2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Datos = pd.read_csv('Tarifas por zonas 2016-2017.csv')

#Muestreo de los datos generales  
print (Datos.info())
print (Datos.describe())
print (Datos.head())

# Para su uso correcto pasar las culumnas de la fecha a datetime donde tendran el formato 
Datos['fecha_inicio'] = pd.to_datetime(Datos['fecha_inicio'])
Datos['fecha_fin'] = pd.to_datetime(Datos['fecha_fin'])

# Filtrar por servicio en base firme
servicio_firme_data = Datos[Datos['uso_base_firme'] > 0]

# Ordena por fecha
servicio_firme_data = servicio_firme_data.sort_values(by='fecha_inicio')

# Gráfico
plt.figure(figsize=(12, 6))
plt.plot(servicio_firme_data['fecha_inicio'], servicio_firme_data['uso_base_firme'], 
label='Servicio en Base Firme', marker='o', linestyle='-', color='Green') 

# Añade etiquetas y leyenda
plt.title('Variación de Tarifas (2016-2017)')
plt.xlabel('Fecha')
plt.ylabel('Tarifa (Base Firme)')
plt.legend(loc='upper right', bbox_to_anchor=(1, 1))

# Se muestra la grafica
plt.tight_layout()
plt.show()

#h)	Genera un gráfico de barras que señale máximos y mínimos de las tarifas por mes de cada uno de los dos años 

# Se filtran los datos que esten vacios
tarifas_base_firme = Datos[Datos['uso_base_firme'].notnull()]
#llama a las columnas año y mes para almacenarse en la nueva columna creada
tarifas_base_firme['año'] = tarifas_base_firme['fecha_inicio'].dt.year
tarifas_base_firme['mes'] = tarifas_base_firme['fecha_inicio'].dt.month
# Se usa la funcion groupby para juntar maximos y minimos
tarifas_por_mes = tarifas_base_firme.groupby(['año', 'mes']).agg({'uso_base_firme': ['max', 'min']})

# se reinicia el indice  y crea un nuevo indice numerico
tarifas_por_mes = tarifas_por_mes.reset_index()

# Nombres de los meses
nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Crea un gráfico de barras
fig, ax = plt.subplots(figsize=(12, 8))

#se usa el ciclo for con tal de mostrar los minimos y los maximos de cada mes
for i, (año, mes) in enumerate(zip(tarifas_por_mes['año'], tarifas_por_mes['mes'])):
    max_value = tarifas_por_mes.loc[(tarifas_por_mes['año'] == año) & (tarifas_por_mes['mes'] == mes), ('uso_base_firme', 'max')]
    min_value = tarifas_por_mes.loc[(tarifas_por_mes['año'] == año) & (tarifas_por_mes['mes'] == mes), ('uso_base_firme', 'min')]
    ax.bar(i, max_value, color='#33CD35', label=f'Máximo - {nombres_meses[mes-1]} {año}')
    ax.bar(i, min_value, color='#7E9E06', alpha=0.5, label=f'Mínimo - {nombres_meses[mes-1]} {año}')
    # Seccion de los valores
    ax.text(i, max_value, f'{max_value.values[0]:.4f}', ha='center', va='bottom', color='blue', fontsize=8)
    ax.text(i, min_value, f'{min_value.values[0]:.3f}', ha='center', va='top', color='blue', fontsize=8)

ax.set_xticks(range(len(tarifas_por_mes)))
ax.set_xticklabels([f'{nombres_meses[mes-1]}\n{año}' for año, mes in zip(tarifas_por_mes['año'], tarifas_por_mes['mes'])])
ax.set_xlabel('Mes y Año')
ax.set_ylabel('Tarifas de Uso Base Firme')
ax.set_title('Máximos y mínimos de tarifas en Base Firme (mes)')
ax.legend()
plt.show()


#opcion 2 

# Generar un gráfico de barras que señale máximos y mínimos de las tarifas por mes de cada uno de los dos años.
Datos['Mes'] = Datos['fecha_inicio'].dt.month
Datos['Año'] = Datos['fecha_inicio'].dt.year

resumen_tarifas = Datos.groupby(['Año', 'Mes']).agg({
    'capacidad_base_firme': ['min', 'max']
}).reset_index()

plt.figure(figsize=(12, 6))
bar_width = 0.35
plt.bar(resumen_tarifas['Mes'] - bar_width / 2, resumen_tarifas['capacidad_base_firme']['min'], bar_width, label='Mínimo')
plt.bar(resumen_tarifas['Mes'] + bar_width / 2, resumen_tarifas['capacidad_base_firme']['max'], bar_width, label='Máximo')
plt.title('Máximos y Mínimos Base Firme por Mes')
plt.xlabel('Mes')
plt.ylabel('Capacidad Base Firme')
plt.xticks(resumen_tarifas['Mes'].unique())
plt.legend()
plt.show()