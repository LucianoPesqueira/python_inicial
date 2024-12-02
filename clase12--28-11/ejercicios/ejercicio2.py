"""Visualización personalizada de productos

Agregá una función al sistema explicado en la clase, que permita simular la venta de un producto.

El usuario o usuaria deberá ingresar el código del producto y la cantidad a vender. Si la cantidad en stock es
suficiente, la función debe restar esa cantidad del inventario. Si la cantidad solicitada es mayor a la disponible,
debe mostrar un mensaje de error."""

def mostrar_productos():
    pass
inventario = {}


def mostrar_productos_personalizados():
    print("1. Mostrar todos los productos")
    print("2. Mostrar productos por categoría")
    print("3. Mostrar productos con stock bajo")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_productos()
    
    elif opcion == 2: 
        categoria = input("Ingrese la categoría de productos a mostrar:")

            #key    value
        for codigo, datos in inventario.items(): #inventario es un dict
            if datos['categoria'].lower() == categoria.lower():
                print("Código:", codigo)
                print("Nombre:", datos['nombre'])
                print("Descripción:", datos['descripcion'])
                print("Cantidad:", datos['cantidad'])
                print("Precio:", datos['precio'])
                print("Categoría:", datos['categoria'])
                print("-" * 30)
                
    elif opcion == 3:
        print("Prouctos con stock bajo:")
        for codigo,datos in inventario.items():
            if datos['cantidad'] < 5:
                print("Código:", codigo)
                print("Nombre:", datos['nombre'])
                print("Descripción:", datos['descripcion'])
                print("Cantidad:", datos['cantidad'])
                print("Precio:", datos['precio'])
                print("Categoría:", datos['categoria'])
                print("-" * 30)
    else: 
        print("Opción no válida. Intente nuevamente.")

mostrar_productos_personalizados()