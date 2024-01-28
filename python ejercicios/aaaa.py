#Angel Martin Mezquita Ramirez

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Tarifas por zonas 2016-2017.csv")
# Crear un DataFrame con los datos proporcionados
data = {
    'zona': ['Sur', 'Centro', 'Occidente', 'Golfo', 'Norte', 'Istmo', 'Nacional', 'Nacional con AB'] * 10,
    'capacidad_base_firme': [100, 120, 90, 80, 110, 95, 150, 130] * 10,
    'uso_base_firme': [80, 90, 70, 60, 85, 75, 120, 110] * 10,
    'capacidad_base_temporal': [50, 60, 45, 40, 55, 48, 75, 65] * 10,
    'uso_base_temporal': [40, 45, 35, 30, 42, 38, 60, 55] * 10,
    'maxima_base_interrumpible': [30, 35, 25, 20, 32, 28, 45, 40] * 10,
    'minima_base_interrumpible': [20, 25, 18, 15, 22, 20, 35, 30] * 10,
    'volumetrica': [15, 18, 12, 10, 16, 14, 25, 22] * 10,
    'fecha_inicio': pd.date_range('2022-01-01', periods=80),
    'fecha_fin': pd.date_range('2022-01-31', periods=80)
}

df = pd.DataFrame(data)

# A) Generar un gráfico de línea para visualizar la variación de las tarifas contra el tiempo para los dos años.
plt.figure(figsize=(10, 6))
for zona in df['zona'].unique():
    datos_zona = df[df['zona'] == zona]
    plt.plot(datos_zona['fecha_inicio'], datos_zona['capacidad_base_firme'], label=zona)

plt.title('Variación de la Capacidad Base Firme por Zona')
plt.xlabel('Fecha')
plt.ylabel('Capacidad Base Firme')
plt.legend()
plt.grid(True)
plt.show()

# B) Generar un gráfico de barras que señale máximos y mínimos de las tarifas por mes de cada uno de los dos años.
df['Mes'] = df['fecha_inicio'].dt.month
df['Año'] = df['fecha_inicio'].dt.year

resumen_tarifas = df.groupby(['Año', 'Mes']).agg({
    'capacidad_base_firme': ['min', 'max']
}).reset_index()

plt.figure(figsize=(12, 6))
bar_width = 0.35
plt.bar(resumen_tarifas['Mes'] - bar_width / 2, resumen_tarifas['capacidad_base_firme']['min'], bar_width, label='Mínimo')
plt.bar(resumen_tarifas['Mes'] + bar_width / 2, resumen_tarifas['capacidad_base_firme']['max'], bar_width, label='Máximo')
plt.title('Máximos y Mínimos de Capacidad Base Firme por Mes')
plt.xlabel('Mes')
plt.ylabel('Capacidad Base Firme')
plt.xticks(resumen_tarifas['Mes'].unique())
plt.legend()
plt.show()