'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
15/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''


#leer tres numeros enteros H, M, S que contienen, Hora, minutos y segundos respectivamente, y comprobar si la hora que se le indica es una hora valida 

# se ingresan valores iniciales
h=0
m=0
s=0

 # se pide un numero a seleccionar que tiene que uno valido
h = int(input("ingresa una hora valida: "))
# si hora es mayor a 24 entonces no es valido y se tiene que volver a poner el numero
if h > 24: #formato de 24 horas 
    # se vuelve a pedir un numero
    print("ERROR")
    # se inicializa un ciclo while donde no te deja avanzar al menor que se ingrese un numero valido
    while h > 24: #formato de 24 horas 
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

