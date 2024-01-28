import pandas as pd 

data = pd.read_csv ("VentasN.csv")
data.head()
data.info()
#sumar los elementos vacios 
data.isnull().sum()
#Eliminar coulumna o campo de codigo postal por tener muchas celdas vacias 
data.drop(['CodigoPostal'], axis=1, inplace=True) #inplace es para hacer el cambio dentro del mismo archivo
#axis sirve para ver si se borra una columnas con 1 o filas con 0 
# 
# Tabla dinamica 
pd.crosstab(data['Segmento'], data['Categoria']) 
pd.crosstab(data['Pais'], data['Subcategoria']) 

#Group by 
data.groupby('Segmento')['Ventas'].sum()
data.groupby('Segmento')['Ventas'].count()
data.groupby(['Segmento', 'Categoria'])['Ventas'].sum()

#Funcion que muestre la suma de las utilidades o benificios por region 
data.groupby('Region')['Beneficio'].sum()

data.groupby['FechaPedido'] = pd.to_datetime 