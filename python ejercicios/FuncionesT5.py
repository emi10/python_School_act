#Comentarios 
#Emilio Antonio Gallegos Bedolla 
#14 de septiembre de 2023
#Funciones 

# paso 1: definir la funcion 
# paso 2: Invocar

def suma():
    a = int(input("Escribe el primer numero: "))
    b = int(input("Escribe el primer numero: "))
    resultado = a + b
    print (resultado)

def sumaR():
    a = int(input("Escribe el primer numero: "))
    b = int(input("Escribe el primer numero: "))
    resultado = a + b
    return resultado #sirve para colocar una variable que se pueda usar , por lo tanto se necesita un objeto para recibir el resultado 

def sumarP(a,b): #ahi se usa atributos donde solo se tiene que colocar los numero que se van a utilizar cuando se vaya a llamar
    return a+b


# invocar a la funcion 
suma() #funcion donde el resultado se muestra porque ya esta en la funcion

final = sumaR() # se usa ese valor para que se guade en un variable y ser reutilizada despues 
print (final)
print (sumaR()) # para mostrar el resultado

resultados = sumarP(5,6) # se ingresa los datos a usar para hacer la suma 
print(resultados)

print(sumarP(5,6)) # o tambien solo puede mostrar los resultados sin variable


a = int(input("Escribe el primer numero: "))
b = int(input("Escribe el primer numero: "))
res = sumarP(a,b) # o tambien se puede pedir llamar la funcion con datos anteriormente utilizados 
print(res) # se guarda en un variable y se muestra






                                                     #Emilio Antonio Gallegos Bedolla
#             EJERCICIO
# Funcion que calcule la base de un Rectangulo, que NO reciba base altura y retorno de area

def calcularareaT():
    b = int(input("Ingresa la base a calcular: "))
    al= int(input("Ingresa la altura a calcular: "))
    retorno = b*al
    print(retorno)

calcularareaT()


# Funcion que calcule la base de un triangulo, que reciba base altura y retorno de area


def calcularareaTi(ba,alt):
    return  ba*alt/2
    

print(calcularareaTi(2,6))