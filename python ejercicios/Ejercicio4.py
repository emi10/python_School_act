#Comentarios 
#Emilio Antonio Gallegos Bedolla 
#12 de septiembre de 2023
#calcular las comisiones sobre ventas, de acuerdo a las ventas mensuales, 
#los vendedores recieben un porsentaje de acuerdo a la siguiente tabla

#ventas > 50000 -> 22%
#ventas > 30001 a 50000 -> 16%
#ventas > 15001 a 30000 -> 10%
#ventas > 8000 a 15000 -> 8%

#Datos de entrada
venta = float(input("Escribe las ventas que realizaste: "))

#proceso     <calcular las comision>
if venta > 50000:
    print("Tendras una comision del 22%")
    comision = venta*.22
elif venta> 30000:
    print("Tendras una comision del 16%")
    comision = venta*.16
elif venta> 15000:
    print("Tendras una comision del 10%")
    comision = venta*.10
elif venta >= 8000:
    print("Tendras una comision del 8%")
    comision = venta*.8
else:
    comision= 0
    print("Suerte para la proxima mi chave")
#Datos de salida
