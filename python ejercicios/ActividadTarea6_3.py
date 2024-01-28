'''
 3.- realizar un programa que defina una clase que permita representar un empleado,
donde cada empleado se define por su identificador del seguro social y nombre,
además de tener un puesto y salario. Los servicios que debe proporcionar la clase son:
captura de datos para nuevos empleados, consultar datos, cambiar puesto o salario.


Utiliza una lista para almacenar las instancias de objetos, construye un menú para que el 
usuario pueda seleccionar el servicio requerido invocando los métodos correspondientes de la clase.
'''
Trabajadores = []

class Empleado:
    def __init__(self, Id, seguro, nombreE, puesto, salario):
        self.Id = Id
        self.seguro = seguro
        self.nombreE = nombreE
        self.puesto = puesto
        self.salario = salario

    # Método para capturar nuevos empleados
    def capturar_empleado(self):
        Trabajadores.append(self)

    # Método para consultar datos
    def consultar_datos(self):
        print("Los datos generales son:")
        print("Identificador del seguro social:", self.seguro)
        print("Nombre del empleado:", self.nombreE)
        print("Puesto del empleado:", self.puesto)
        print("Salario del empleado:", self.salario)

    # Método para cambiar puesto y salario
    def cambiar_puesto_salario(self, nuevo_puesto, nuevo_salario):
        self.puesto = nuevo_puesto
        self.salario = nuevo_salario
        print("Puesto y salario actualizados exitosamente.")

while True:
    print("\nMenú:")
    print("1. Consultar datos de empleado")
    print("2. Ingresar un nuevo empleado")
    print("3. Cambiar el puesto y salario de un empleado")
    print("4. Salir")
    respuesta = int(input("Seleccione una opción: "))

    if respuesta == 1:
        if Trabajadores:
            seguro = input("Ingrese el identificador del seguro social del empleado a consultar: ")
            for empleado in Trabajadores:
                if empleado.seguro == seguro:
                    empleado.consultar_datos()
                    break
            else:
                print("Empleado no encontrado.")
        else:
            print("No hay empleados registrados.")
    
    elif respuesta == 2:
        Id = input("Ingrese el identificador del empleado: ")
        seguro = input("Ingrese el identificador del seguro social: ")
        nombreE = input("Ingrese el nombre del empleado: ")
        puesto = input("Ingrese el puesto del empleado: ")
        salario = int(input("Ingrese el salario del empleado: "))
        nuevo_empleado = Empleado(Id, seguro, nombreE, puesto, salario)
        nuevo_empleado.capturar_empleado()
        print("Empleado registrado exitosamente.")

    elif respuesta == 3:
        if Trabajadores:
            seguro = input("Ingrese el identificador del seguro social del empleado a actualizar: ")
            for empleado in Trabajadores:
                if empleado.seguro == seguro:
                    nuevo_puesto = input("Ingrese el nuevo puesto: ")
                    nuevo_salario = int(input("Ingrese el nuevo salario: "))
                    empleado.cambiar_puesto_salario(nuevo_puesto, nuevo_salario)
                    break
            else:
                print("Empleado no encontrado.")
        else:
            print("No hay empleados registrados.")

    elif respuesta == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
