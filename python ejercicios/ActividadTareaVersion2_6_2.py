'''
Ejercicio 2
Crea un procedimiento para hacer una barra de progreso. El procedimiento deberá incluir lo siguiente:

Aceptar un número entre el 0 y 100.
Imprimir el porcentaje de avance mediante el mensaje: Progreso: __%
En una línea nueva se deberán visualizar los símbolos de gato (#) igual a la cantidad ingresada en el punto anterior.
Mostrar guiones suficientes para completar los 100 caracteres en la misma línea.
Se pueden agregar pipes (|) al inicio y final de la barra de progreso (opcional).


ESTA ES OTRA VERSIÓN DEL EJERCICIO 2 DE LO QUE SE PUEDO HABER HECHO
'''
# se crea una lista donde van hacer almacenados el simbolo de la carga 
lista_Carga = []

# se le da la opcion al usuario si quiere iniciar con el procedimiento
progreso = int(input("Quieres iniciar con la descarga? \n 1 = si, 2 = no"))

# si el ususario selecciona el numero 1 entonces incia con el proceso normal 
if progreso == 1:
    # se hace un ciclo que hace 10 veces donde y se iran actualizacndo los datos
    for w in range(0,10):
        #se almacena en la lista en simbolo "#"
        lista_Carga.append ("#")
        # y muestra la lista 
        print("".join(lista_Carga),"%")
        
#si el usuario usa la opcion 2 entonces solo se finalizara el codigo 
elif progreso == 2:
     print ("entendido, que tenga buen dia ╰(*°▽°*)╯")

#si no se elige ninguna de las dos entonces se dira que esta esta mal y se le volvera a pedir al usuario poner otro valor
else: 
    progreso = int(input("Vuelve a ingresar una opcion valida: "))
    #se repiete todo el procedimiento de la opcion 1
    while progreso == 1 or progreso == 2:
        for w in range(0,10):
            lista_Carga.append ("#")
            print("".join(lista_Carga),"%")



