#Comentarios 
#Emilio Antonio Gallegos Bedolla 
#12 de septiembre de 2023
#Ejercicio de pruebas de sentencia de control repetitivas FOR y WHILE

#for
texto = "hola"
for q in texto: 
    print(q)

for w in range(10):
    print(w)

for w in range(1,11):
    print(w)

for y in range(5,101,10):
    print(y)

#for y(es una variable a llamar) in range(dentro de un rango de o hacer el conteo del objeto puesto)(inicia en 5, termina en 101, y va de 10 en 10):
#    print(y)
#  

#imprimir una tabla de multiplicacion, pedir al usuario que lo ponga el numero a usar

numeromul = int(input("Que numero quieres usar para multiplicar"))

for s in range(1,11):
    print (numeromul,"x",s, " = ",numeromul*s)


#calcular el promedio de 5 numeros del usuario


for g in range(5):
    numeros = int(input("escribe un numero: ")) 
    acumulador = acumulador + numeros
promedio = acumulador/5
print ("el promedio es de: ",promedio)
