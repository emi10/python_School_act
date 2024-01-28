import sqlite3

opcion = True

while opcion:
    print("Para acceder a las funciones de la aplicación, se necesita aceptar la ubicación del usuario.")
    respuesta = int(input("1 = sí, 2 = no: "))

    if respuesta == 1:
        locacion = input("Seleccione la calle que desea ver su estado: ")

        conn = sqlite3.connect('charts.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM nombre_de_la_tabla WHERE NombreDeCalle = ?", (locacion,))
        resultados = cursor.fetchall()

        for row in resultados:
            print("ID:", row[0])
            print("Nombre de la Calle:", row[1])

        conn.close()
        
        opcion = False
    elif respuesta == 2:
        print("El sistema no se puede inicializar sin los permisos")

    else: 
        break

