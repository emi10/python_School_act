'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
15/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''

'''Escribe un programa que contenga dos funciones, crea una funcion llamada distancia, que recibira 4 parametros que consisten en las coprdenadas de 2 puntos en el plano cartesiano.
La funcion devolvera la distancia entre los dos puntos dados. Crea una segunda funcion que convierte de grados Celsius a Fahrenheit, tomara los grados Celsius y retonara Fahrenheit.
incluir 2 pruebas del funcionamiento '''

import math

def distancia (x1,x2,y1,y2):
    distancia = math.sqrt((x2-x1)**2+ (y2-y1)**2)
    print("La distancia entre los puntos es de: ",distancia)
    return distancia

x1 = int(input("ingresa el primer dato de x1: "))
x2 = int(input("ingresa el primer dato de x2: "))
y1 = int(input("ingresa el primer dato de y1: "))
y2 = int(input("ingresa el primer dato de y2: "))


distancia(x1,x2,y1,y2)

def grados (c):
    f= (c*9/5)+32
    print("los grados Fahrenheit son: ",f)
    return f

c= float(input("ingresa los grados Celsius para transformar a Fahrenheit: "))
grados(c)
