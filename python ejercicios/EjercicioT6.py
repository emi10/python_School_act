'''
Actividad 5 Big Data
Emilio Antonio Gallegos Bedolla
21/09/2023
solucionar los siguientes problemas y realizar su codificacion en python
'''

#Archivo txt
archivo = open ("EresMiLuz.txt",'r')
#lee el archivo como un String 
datos = archivo.read()
print(datos)
# Cierra el archivo
archivo.close()

#Archivo txt
archivo = open ("EresMiLuz.txt",'r')
#lee el archivo como una lista  
lista = archivo.readlines()

for x in range:
    print(x)

archivo.close()


#Escribir en un archivo de Texto 
archivo = open ("Archivo Renuevo.txt", 'w')
#escribir en un archivo 
archivo.write("probando escribir en texto en archivo...")
archivo.write("Hola ")
archivo.close()

#Escribir una lista en un archivo 
archivo = open ("Archivo Renuevo.txt", 'a')
# Escribir el nombre en un archivo 
nombres = ["Emilio\n, Antonio\n, Ricardo\n, Jose\n, Adrian\n, "]
archivo.writelines(nombres)
archivo.close()

#Abrir el archivo con with
with open ("Archivo Renuevo.txt", 'r') as archivo:
    datos = (archivo.read())

    # solo se ahorra el close 

#escribir en un archivo .csv
import csv
produtos = [("lampara",1234,6),("mesa",8900,3),("Silla",3456,12)]

with open("productos.csv",'w', newline= ("\n")) as archivo:
    escribir = csv.writer(archivo, delimiter= ",")
    for x in produtos:
        escribir.writerow(x)