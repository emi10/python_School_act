'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
15/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''

'''Realiza un juego para adivinar un numero. para ello pedir un numero,
 si el numero no es el correcto se va a seguir pidiendo numeros indicando 'mayor'
   o menor y el proceso termina cuando el usario acierta '''

import random

print("GENERANDO EL NUMERO ALETORIO...")
# Se crea la variable random y se especifica sus limites
n_A = random.randint(1,10)
#Entrada de datos de la respuesta del usuario
Respuesta=int(input("Entre el 1 al 10 \n ¿Que numero crees que es? \n(Responde con sabiduria)"))
# su la respuesta es diferente tu respuesta entonces se va volver a preguntar y se dira si estas cerca o lejos
while Respuesta != n_A:
    if Respuesta > n_A:
        print("El numero es menor")
    else: 
        print ("El numero es mayor")
    Respuesta = int(input("Vuelve a intentarlo"))
    # si la respuesta es la misma al numero elegido entonces, se te felicita
print("El numero es: ",n_A)
print("Correcto, bien jugado")