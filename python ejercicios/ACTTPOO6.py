'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
21/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''
"Generar una contrase;a donde se le pida al usuario cuantas letras, numero y simbolos quiere y colocarlo de forma aleatoria"

import random
Le_nu = int(input("Cuantas letras quieres en tu contrasena: "))
Nu_nu = int(input("Cuantas numeros quieres en tu contrasena: "))
Si_nu = int(input("Cuantas simbolos quieres en tu contrasena: "))

contrasena = [] 
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
 'Y', 'Z'] 
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


for w in range (Le_nu):
 elementos_letra = random.choice(letras)
 contrasena.append(elementos_letra)

for r in range (Nu_nu):
 elementos_numero = random.choice(numeros)
 contrasena.append(elementos_numero)

for t in range (Si_nu):
  elementos_simbolos = random.choice(simbolos)
  contrasena.append(elementos_simbolos)

random.shuffle(contrasena)
contrasena_Aleatoria = "".join(contrasena)
print (contrasena_Aleatoria)
 