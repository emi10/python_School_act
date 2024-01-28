
#Emilio Antonio Gallegos Bedolla 
#17 de Octubre de 2023
#Ejercicios de las libreria Panda 

# Manipular y analizar Datos 
# Dos estructuras de datos: Series y Dataframes 

# Series : unidimencionales, indice 
# Dataframes: Bidimencionales, indices 

import pandas as pd
#Series
numeros = pd.Series([1,2,3,4,5,6,7])
print(numeros)
print(numeros[3])
#Diccionarioa  a serires
dicc={'a':100,'b':200,'c':300,'d':400,'e':500}
valores=pd.Series(dicc)
print(valores)
print(valores['d'])

#dataframe
datos  = {'nombre': ['Luis', 'Maria', 'Carlos', 'Jaime', 'Bruno', 'Cindy', 'Mateo', 'Laura', 'Guadalupe', 'Julio'],
        'score': [12.5, 9, 16.5, 5, 9, 20, 14.5, 10, 8, 19],
        'intentos': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'califica': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
etiquetas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(datos,index=etiquetas)
print(df)
df2 = pd.DataFrame(datos)
print(df2)

#Manipulación de dataframe
#Ver columnas especificas
print(df[['nombre','score']])
#Especifico con condiciones
print(df[df['intentos']>=2])
#Contar filas y columnas
totalf = len(df.axes[0]) #PARA COLUMNAS 1 Y FILAS 0
totalc = len(df.axes[1])
print("total de filas: ",totalf)
print("total de columnas: ",totalc)
#Especifico con condiciones con between
print(df[df['score'].between(15,20)])
#Especifico con condiciones con mean osea promedio
print(df['score'].mean())
#Especifico con condiciones con maximo y minimo
print(df['score'].max())
print(df['score'].min())
#Ordenar
print(df.sort_values(by=['nombre']))
print(df.sort_values(by=['nombre'],ascending=False))

#Agrupar hay que saber donde aplicarlo, intentos por si solo no funciona
#Agrupación por intentos
resultado = df.groupby(['intentos'])
for name, group in resultado:
    print('\nGrpo:')
    print(name)
    print(group)

#Por califica
resultado2 = df.groupby(['califica'])
for name, group in resultado2:
    print('\nGrpo:')
    print(name)
    print(group)

#Campo no adecuado para agrupar
resultado3 = df.groupby(['nombre'])
for name, group in resultado3:
    print('\nGrpo:')
    print(name)
    print(group)