'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
15/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''
import random
import math


#leer tres numeros enteros H, M, S que contienen, Hora, minutos y segundos respectivamente, y comprobar si la hora que se le indica es una hora valida 

# se ingresan valores iniciales
h=0
m=0
s=0

 # se pide un numero a seleccionar que tiene que uno valido
h = int(input("ingresa una hora valida: "))
# si hora es mayor a 24 entonces no es valido y se tiene que volver a poner el numero
if h > 25: #formato de 24 horas 
    # se vuelve a pedir un numero
    print("ERROR")
    # se inicializa un ciclo while donde no te deja avanzar al menor que se ingrese un numero valido
    while h > 25: #formato de 24 horas 
        h = int(input("Numero no valido, intentelo de nuevo \n Ingresa otra hora: "))
else:
    # de ser correcto se siguie con la siguiente parte y se repite el ciclo de la primera parte
    print("correcto, pasemos ahora a ingresar un minuto")
    


m = int(input("ingresa un minuto valido: "))
if m > 61:
    print("Numero incorrecto vuelva a intentarlo")
    while m > 61:  
        m = int(input("Numero no valido, intentelo de nuevo \n Ingresa otro minuto: "))

else:
        # se repite la el mismo cliclo que la primera parte
    print("Correcto ahora pasemos a ingresar un segundo ")


s = int(input("ingresa un segundo valido: "))
if s > 61:
    print("Numero incorrecto vuelva a intentarlo")
            # cambiar por un ciclo while
    while s > 61:
        s = int(input("Numero no valido, intentelo de nuevo \n Ingresa otro segundo: "))
else:
    print("") # se muesta la hora final
            
# se muesta la hora final
print("Su hora ingresada es :",h,":",m,":",s)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////


"pedir al usuraio 8 numeros. mostrar al final el promedio de los numeros positivos y el promedio de los numero negativos y la cantidad de ceros "
# se especifican las variables a utilizar 
promedio = 0
# se usa un ciclo for para pedir un dato una derteminada cantidad de veces 
for x in range(8):
    # dentro de ella, se pide un numero 8 veces
    numero = float(input("ingresa un numero: "))
    # se alamacena la variable antes especificada 
    promedio = promedio + numero
# se hace la operacion a realizar
Resultado = promedio/8 
# se muestran los datos 
print("el promedio de los numero es de: ", Resultado)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

'''Realiza un juego para adivinar un numero. para ello pedir un numero,
 si el numero no es el correcto se va a seguir pidiendo numeros indicando 'mayor'
   o menor y el proceso termina cuando el usario acierta '''

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
print("Correcto, bien jugado")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

'''dadas las edades y alturas de N alumnos, mostrar la edad y la estatura media, 
cantidad de alumnos mayores a 18 años y la cantidad de alumnos que miden más de 1.70,
 preguntar al usuario el numero de alumnos''' 

#entrada de datos
# se especifican las listas donde se van a guardar las variables 
lista_Alumnos_Edad = []
lista_Alumnos_Alt = []
lista_Alumnos_EM = []
lista_Alumnos_AM = []

# se ingresa la cantidad de alumnos a analizar 
Numero_Alumnos= int(input("¿Cuantos alumnos quieres saber sobre su estatura y edad? "))
# se usa el ciclo for donde con la variable Numero_Alumnos se indicara la cantidad de veces para preguntar sobre su edad y estatura
for w in range(Numero_Alumnos):
    edad = int(input("ingresa Edad del Alumno: "))
    if edad >= 18:
        #si la edad es igual o mayor a 18 se guarda en la su lista correspondiente 
        lista_Alumnos_Edad.append(edad)
    # si la edad es guarda en otra lista
    else:
        lista_Alumnos_EM.append(edad)

    altura = float(input("ingresa altura del Alumno: ")) 
    if altura >= 1.70:
        #si la altura es igual o mayor a 1.70 se guarda en la su lista correspondiente
        lista_Alumnos_Alt.append(altura)
    # si no lo es se guarda en otra lista
    else:
        lista_Alumnos_AM.append(altura)
        
# se cuentan la cantidad de gente que se ingreso en sus listas 
can_Alu_Altura = len(lista_Alumnos_Alt)
can_Alu_AM = len(lista_Alumnos_AM)
can_Alu_Edad = len(lista_Alumnos_Edad)
can_Alu_EM = len(lista_Alumnos_EM)

# se muestra el usuario el numero de personas por lista 
print("Numero de alumnos mayores a 18 años: ", can_Alu_Edad)
print("Numero de alumnos menores a 18 años: ", can_Alu_EM)
print("Numero de alumnos mayores a 1.70: ", can_Alu_Altura)
print("Numero de alumnos menores a 1.70: ", can_Alu_AM)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

'''Escribe un programa que contenga dos funciones, crea una funcion llamada distancia, que recibira 4 parametros que consisten en las coprdenadas de 2 puntos en el plano cartesiano.
La funcion devolvera la distancia entre los dos puntos dados. Crea una segunda funcion que convierte de grados Celsius a Fahrenheit, tomara los grados Celsius y retonara Fahrenheit.
incluir 2 pruebas del funcionamiento '''

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