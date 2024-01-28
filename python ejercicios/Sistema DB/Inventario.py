from Base_Datos import BaseDatos
import sqlite3

class AdministracionInventario:
    def __init__(self):
        self.baseDatos = BaseDatos('inventario.db')
        if self.baseDatos.verificacionBD () == False:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTabla()

    def mostrarProductos(self):
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        for x in productos:
            print (x)
        
        cursor.close()
        conexion.close()

    def agregarProducto(self):
        conexion=sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        #Pedir datos al usuario
        nombre = input("Ingresa el nombre del producto: ")
        descripcion = input("Ingresa descripción del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        stock = int(input("Ingresa el stock del producto: "))
        
        valores = (nombre, descripcion, precio, stock)
        sql = ''' INSERT INTO productos(nombre,descripcion,precio,stock)
                    VALUES(?,?,?,?) '''
        cursor.execute(sql,valores)
        conexion.commit()
        print("Datos guardados correctamente")
        cursor.close()
        conexion.close()

    
    def modificarProducto(self):     
        
        conexion=sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        self.mostrarProductos()
        print("----------------------------------")
        id_producto = input("Ingresa el id del producto a modificar ")
                
        encontrar_producto = cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))    
        producto = encontrar_producto.fetchone()
        if producto :
            #Pedir datos al usuario
            nombre = input("Ingresa el nombre del producto: ")
            descripcion = input("Ingresa descripción del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            stock = int(input("Ingresa el stock del producto: "))

            sql = ''' UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, stock = ? WHERE id = ? '''
            datos_producto = (nombre,descripcion,precio,stock,id_producto)
            cursor.execute(sql,datos_producto)
            conexion.commit()
            print("Registro modificado correctamente")
                    
        else:
            print("No hay registro con ese id")
        cursor.close()
        conexion.close()





    def eliminarProducto(self):


        conexion=sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        print("Lista de productos para eliminar:")
        self.mostrarProductos()
        print("------------------------------------")
        id_producto = input("Ingresa el id del producto a eliminar \n")
        encontrar_producto = cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))     
        if len(encontrar_producto.fetchall()) == 1:
            sql = ''' DELETE FROM productos WHERE id = ? '''
            cursor.execute(sql,(id_producto,))
            conexion.commit()
            print("Registro eliminado correctamente")
                    
        else:
            print("No hay registro con ese id")
        cursor.close()
        conexion.close()

