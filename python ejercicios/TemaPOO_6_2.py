#Comentarios 
#Emilio Antonio Gallegos Bedolla 
#19 de septiembre de 2023
#POO PROGRAMACIÓN ORIENTADA A OBJETOS 

#Clase Rectangulo con dos atributos y dos metodos: Calcular area y calcular el perimetro


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Comportamientos
    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self):
        perimetro = 2 * self.base * 2 *  self.altura
        return perimetro
    
    def __str__(self):
        desplegar = "La base es: " + str(self.base) + "La altura es de: " + str(self.altura)
        return desplegar

prueba = Rectangulo(77, 23)
print(prueba.area())
print (prueba.perimetro())
print(prueba)


