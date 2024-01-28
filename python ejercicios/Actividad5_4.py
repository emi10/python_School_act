'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
15/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''

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