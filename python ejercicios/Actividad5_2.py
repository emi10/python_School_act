'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
15/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''

"pedir al usuraio 8 numeros. mostrar al final el promedio de los numeros positivos y el promedio de los numero negativos y la cantidad de ceros "

# se especifican las variables a utilizar 
promedio = 0
ceros = 0 
# se usa un ciclo for para pedir un dato una derteminada cantidad de veces 
for x in range(8):
    # dentro de ella, se pide un numero 8 veces
    numero = float(input("ingresa un numero: "))
    # se alamacena la variable antes especificada 
    promedio = promedio + numero
    # la funcion if determina que si hay ceros en los datos, los va a contar
    if numero == 0:
        # se almacenan en la variable ceros
        ceros= ceros + 1
# se hace la operacion a realizar
Resultado = promedio/8
ResultadoN = promedio/-8
# se muestran los datos 
print("el promedio de los numero es de: ", Resultado)
print("el promedio de los numero es de: ", ResultadoN)
print("La cantidad de cero es de: ", ceros)


