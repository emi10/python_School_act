#Comentarios 
#Emilio Antonio Gallegos Bedolla 
#14 de septiembre de 2023
#Ejercicio de pruebas de sentencia de control repetitivas WHILE

#while

#promedio de 5 nuemeros
i = 0
while i < 11:
    print(i)
    i = i + 1

# pedir numeros y sumarlos hasta que el usuario precione un cero 
suma= 0
numero = 1 
while numero != 0:
    numero = int(input("Inserta numero a sumar: "))
    suma = suma + numero

print ("El numero final es: ",suma)

# pida numero hasta que la suma de los mismos sea mayor a 100

suma= 0
numero = 1 
while suma <= 100:
    numero = int(input("Inserta numero a sumar: "))
    suma = suma + numero

print ("El numero final es: ",suma)


#Emular do While 

calculo = 0
nume = 1
while True:
    nume = int(input("Inserta numero a sumar: "))
    calculo = calculo + nume
    if calculo >= 100:
        break
print("Tu suma es de: ",calculo)

