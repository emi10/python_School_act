#Comentarios 
#Emilio Antonio Gallegos Bedolla 
#31 de Agosto de 2023
#Cálculo de el área de un triangulo
#Trabajar con IF doble
# Calcular un bono a empleados que han trabajado más de 4 en la empresa
#bono =500, para los otros Bono = 100

#Datos de entrada
Antiguedad = int(input("ingresa tu tiempo en tu trabajo"))
sueldobase = int (input("Cuanto ganas normalmente?"))

#Proceso
if Antiguedad >= 4:
    print("tu sueldo de de", sueldobase + 500)
else:
    print("tu sueldo es de ", sueldobase + 100)