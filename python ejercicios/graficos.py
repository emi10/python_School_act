#Ejercicios de gráficos con matplotlib

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('titanic.csv')
#EDA
data.shape
data.columns
data.info()
data.head()
data.tail()
data.isna()
data.isna().sum()
data.describe()

#Eliminar columa o variable
data.drop('PassengerId', axis=1,inplace=True)

#Tabla cruzad
pd.crosstab(data['Survived'],data['Sex'])
#Tablas
data['Survived'].value_counts()
#Tabla de frecuencia con pandas
data.groupby('Survived').count()
data.groupby('Survived')['Survived'].count()

#Grafico de sobreviviente
data['Survived'].value_counts().plot.bar(title="Grafico de Sobrevivientes",xlabel = "Sobrevivientes", ylabel = "Frecuencia")

#Matplotlib
dataClass = data.groupby('Pclass').count()
#Definir ejes
ejex = dataClass.index.to_list()
ejey = dataClass['Survived'].to_list()

#Crear gráficos
plt.locator_params('x',nbins=3)
plt.bar(ejex,ejey)
plt.ylabel('Frecuencia')
plt.xlabel('Clases')
plt.title('Grafica de sobreviviengtes por clase')

#Barras horizontales
data['Sex'].value_counts().plot.barh(alpha=0.5,title="Grafico por sexo")
#barra normal
data['Sex'].value_counts().plot.bar(alpha=0.5,title="Grafico por sexo")

#Matplotlib
plt.locator_params('x',nbins=3)
plt.barh(ejex,ejey)
plt.ylabel('Frecuencia')
plt.xlabel('Clases')
plt.title('Grafica de sobreviviengtes por clase')

#Histograma
#Matplotlib
plt.hist(data['Age'],bins=20)
plt.ylabel('Frecuencia')
plt.xlabel('Edad')
plt.title('Histograma de edades')

#Boxplot
data.boxplot(column='Age').plot()
plt.title('Variable edad')