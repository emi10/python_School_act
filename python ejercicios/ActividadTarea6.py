'''
Actividad 6 Big Data
Emilio Antonio Gallegos Bedolla
22/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''


'''
Ejercicio 1

Crea dos cadenas una con tu nombre y otra con tu apellido.
Asigna las cadenas a las variables nombre y apellido respectivamente.
Concatena ambas variables e imprime el resultado usando print ()
'''
#se pide el primer al usuario que ingrese su nombre o nombres
nombre = str(input("Ingresa tu nombre \no de tener mas de un nombre, colocar ambos: "))
#se le pide al susuario sus apellidos
apellidos = str(input("Ingresa tus apellidos: "))
#se juntnan el o los nombres y los apellidos del usuario escribio
nombreCompleto = print("Entonces, tu nombre es: " + nombre +" "+ apellidos + " ¿Estoy en lo correcto?")




'''
Ejercicio 2 version 2
Crea un procedimiento para hacer una barra de progreso. El procedimiento deberá incluir lo siguiente:

Aceptar un número entre el 0 y 100.
Imprimir el porcentaje de avance mediante el mensaje: Progreso: __%
En una línea nueva se deberán visualizar los símbolos de gato (#) igual a la cantidad ingresada en el punto anterior.
Mostrar guiones suficientes para completar los 100 caracteres en la misma línea.
Se pueden agregar pipes (|) al inicio y final de la barra de progreso (opcional).

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
    



'''
 3.- realizar un programa que defina una clase que permita representar un empleado,
donde cada empleado se define por su identificador del seguro social y nombre,
además de tener un puesto y salario. Los servicios que debe proporcionar la clase son:
captura de datos para nuevos empleados, consultar datos, cambiar puesto o salario.


Utiliza una lista para almacenar las instancias de objetos, construye un menú para que el 
usuario pueda seleccionar el servicio requerido invocando los métodos correspondientes de la clase.
'''

Trabajadores = []
class empleado:
    def __init__(self, Id,seguro,nombreE,puesto,salario):
        self.Id = Id
        self.seguro = seguro
        self.nombreE = nombreE
        self.puesto = puesto
        self.salario = salario

#comportamientos de la clase

#captura para nuevos empleados 

    def nuevosEmpleados (self):
        Id = str(input("ingresa su identificador: ")) 
        Trabajadores.append(Id)
        seguro = str(input("ingresa su identificador del seguro social: "))
        Trabajadores.append(seguro)
        nombreE = str(input("Nombre del nuevo trabajador: "))
        Trabajadores.append(nombreE)
        salario = int(input("ingresa el salario del trabajador: "))
        Trabajadores.append(salario)

#consultar datos
    def consulta (self):
        print("Los datos generales son: ")
        print("Identificados de los usuarios", self.Id)
        print("El nombre de los usuarios: ",self.nombreE)
        print("Puesto de los trabajadores",self.puesto)
        print("salarios de los trabajadores",self.salario)
        

#cambiar puesto o salario
    def cambio (self):
        puesto = str(input("ingrese el nuevo puesto: "))

        salario = int(input("ingresa el nuevo salario a cambiar: "))