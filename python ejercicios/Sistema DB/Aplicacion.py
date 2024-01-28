from Inventario import AdministracionInventario

class Aplicacion:
    
    def __init__(self):
        self.iniciarAplicacion()
    
    def iniciarAplicacion(self):
        inicio = AdministracionInventario() #
        
        salir_programa = False
        while not salir_programa:
            print("Menú del inventario")
            print(""" 
                1.- Mostrar lista de productos
                2.- Agregar producto
                3.- Modificar producto
                4.- Eliminar producto
                5.- Salir del programa
                """)
            opcion = int(input("Indica una opción del menú "))
            if opcion == 1:
                inicio.mostrarProductos()
            elif opcion == 2:
                inicio.agregarProducto()
            elif opcion == 3:
                inicio.modificarProducto()
            elif opcion == 4:
                inicio.eliminarProducto()
            if opcion == 5:
                print("Salida del programa, hasta luego ")
                salir_programa = True
                
sistema_inventario = Aplicacion()