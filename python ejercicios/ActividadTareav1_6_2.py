'''
Ejercicio 2
Crea un procedimiento para hacer una barra de progreso. El procedimiento deberá incluir lo siguiente:

Aceptar un número entre el 0 y 100.
Imprimir el porcentaje de avance mediante el mensaje: Progreso: __%
En una línea nueva se deberán visualizar los símbolos de gato (#) igual a la cantidad ingresada en el punto anterior.
Mostrar guiones suficientes para completar los 100 caracteres en la misma línea.
Se pueden agregar pipes (|) al inicio y final de la barra de progreso (opcional).

'''
# se le pregunta al usuario si quiere iniciar el sistema
progreso = int(input("Quieres iniciar con la descarga? \n 1 = si, 2 = no"))
# de elegir 1 se inicia
if progreso == 1:
    # se le pide cual va hacer la cantidad de avance de la barra de carga del sistema 
    porcentaje = int(input("ingrese la cantidad del avance: "))
    # se le da un minimo el cual va hacer el 0 y el maximo el cual es 100, ademas de tomar en cuenta el porcentaje que nosotros elegimos 
    porcentaje = max(0,min(100,porcentaje))
    #se va a mostrar el progreso que nosotros elegimos mas el simbolo del porcentaje 
    print("progreso",porcentaje, "%")
    #se especifica el valor del avance de la que va hacer el porcentaje que nosotros especificamos anteriormente
    avance = porcentaje
    #se especifica la cantidad que va haber pero se va arrestar con el avance osea el porcentaje que nosotros elegimos para que no se acumule y siga siendo 100
    cantidad = 100 - avance
    #ya solo se muesta el resultado de la barra 
    print("|" + "#" * avance + "-" * cantidad + "|")

#si se eleige la opcion 2 entonces solo se finaliza el sistema 
elif progreso == 2:
    print ("entendido, que tenga buen dia ╰(*°▽°*)╯")

#si se elige cualquier numero que no sea el 1 u 2 entonces se te va volver a pedir que se seleccione uno de los valores establecidos
else: 
    progreso = int(input("Vuelve a ingresar una opcion valida: "))
# se pide el valor y si no es 1 o 2 entonces se va a repetir esta peticion hasta que se tome el numero correcto 
    while progreso != 1 or progreso != 2:
        progreso = int(input("Vuelve a ingresar una opcion valida: "))

    #depues de esto ya solo se vuelve arrepetir lo mismo que el punto numero 1
    porcentaje = int(input("ingrese la cantidad del avance: "))
    porcentaje = max(0,min(100,porcentaje))
    print("progreso",porcentaje, "%")
    avance = porcentaje
    cantidad = 100 - avance
    print("|" + "#" * avance + "-" * cantidad + "|")

