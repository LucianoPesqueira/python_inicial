#Diccionario para almacenar los productos
productos = {}

#Función para registrar un producto
def registrar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    productos[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' registrado con éxito.\n")

#Función para consultar un producto
def consultar_producto():
    codigo = input("Ingrese el código del producto a consultar: ")
    if codigo in productos:
        producto = productos[codigo]
        print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}\n")
    else: 
        print("El producto no existe, volve a intentarlo.\n")
        
#Función para actualizar un producto
def actualizar_producto():
    codigo = input("Ingrese el código del producto a actualizar: ")
    if codigo in productos:
        print("Ingrese los nuevos datos del producto:")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad:"))
        precio = float(input("Precio:"))
        productos[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        print(f"Producto '{nombre}' actualizado con éxito.\n")
    else: 
        print("El producto no existe, volve a intentarlo.\n")

#Función para eliminar un producto
def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    if codigo in productos:
        del productos[codigo]
        print(f"Producto eliminado con éxito.\n")
    else: 
        print("El producto no existe, volve a intentarlo.\n")

#Función para listar todos los productos
def listar_productos():
    if productos:
        print("Lista completa de productos:")
        for codigo, datos in productos.items():
            print(f"Código: {codigo}, Producto: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")
        print()
    else:
        print("No hay productos registrados.\n") 

#Función para mostrar productos con bajo stock
def reporte_bajo_stock():
    limite = int(input("Ingrese el límite de stock bajo: ")) 
    productos_bajo_stock = {k: v for k, v in productos.items() if v['cantidad'] < limite}
    if productos_bajo_stock:
        print("Producto con bajo stock: ")
        for codigo, datos in productos_bajo_stock.items():
            print(f"Código: {codigo}, Producto: {datos['nombre']}, Cantidad: {datos['cantidad']},")
        print()
    else:
        print("No hay productos con bajo stock.\n")


#Menú interactivo
def menu():
    while True:
        print("Menú de opciones:")
        print("1. Registrar producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("6. Reporte de bajo stock")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            listar_productos()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Saliendo del programa, chau chau...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

#Ejecutar el menú
menu()