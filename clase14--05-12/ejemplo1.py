#menu

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
#menu()

# MENU 2

productos = {}

def registrar_producto(): 
    print("Registro")
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    productos[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio} #{'000': {'nombre': 'teclado', 'cantidad': 24, 'precio': 123.56}}
    print(f"Producto '{nombre}' registrado con éxito.\n")
    
    
def consultar_producto():
    print("consultar")
def actualizar_producto():
    print('actualizar')
def eliminar_producto():
    print("eliminar")
def listar_productos():
    print("listar")
def reporte_bajo_stock():
    print("reporte")
    

#opc_list almacena referencias a las funciones
opc_list = [registrar_producto, consultar_producto, actualizar_producto, eliminar_producto, listar_productos, reporte_bajo_stock]

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
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion < 1 or opcion > 7:
            print("Error, opcion incorrecta")
        elif opcion == 7:
            print("salir del sistema...")
            break
        else:
            opc_list[opcion -1]()
        
  
menu()