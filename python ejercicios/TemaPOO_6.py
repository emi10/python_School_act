#Comentarios 
#Emilio Antonio Gallegos Bedolla 
#19 de septiembre de 2023
#POO PROGRAMACIÓN ORIENTADA A OBJETOS 

#Clase Auto 

class auto:
    def __init__(self, marca, modelo, color, placa ): # Es un constructor y esa es su suntaxis 
        self.marca = marca 
        self.modelo = modelo
        self.color = color
        self.placa = placa

    #Comportamiento
    def Encender (self):
        print("Encendido")
    def Apagar (self):
        print ("Apagado")

    def Desplegar (self):
        print("La marca del carro es: ", self.marca)
        print("El modelo del carro es: ", self.modelo)
        print("El color del carro es: ", self.color)
        print("La mplaca del carro es: ", self.placa)
#Pruebas para la instancia de los objetos 

Auto1 = auto("kia",2018,"Rojo"," NRU905B")

# Lo que muestra

print(Auto1.color)

Auto1.Encender()

Auto1.Apagar()

Auto1.Desplegar()
        



