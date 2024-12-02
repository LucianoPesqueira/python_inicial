"""Registro de productos con validaciones

Escribí una función que permita registrar un nuevo producto en el inventario, pero con una condición: la
cantidad de productos debe ser mayor que 0 y el precio también debe ser un valor positivo.

Al ingresar una cantidad o precio no válido, debe mostrar un mensaje de error y pedir los datos nuevamente
hasta que sean correctos."""
producto = {}
def registrar_producto():
    global codigo_actual
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad <= 0:
                print("Ingrese una cantidad mayor a 0")
            else:
                break
        except ValueError:
            print("Error, la cantidad ingresada no es valida!!")
    
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("Ingrese un precio mayor a 0")
            else:
                break
        except ValueError:
            print("Error, el precio ingresada no es valida!!")
            
    producto = {
        "nombre" : nombre,
        "descripcion" : descripcion,
        "cantidad" : cantidad,
        "precio" : precio
    }
    
    print("Producto registrado con exito!!\n")
    return producto


productos = registrar_producto()

for key, value in productos.items():
    print(key, value)
