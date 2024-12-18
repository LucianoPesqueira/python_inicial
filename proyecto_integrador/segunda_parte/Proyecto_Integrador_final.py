import sqlite3
from colorama import init, Fore, Back, Style

# Inicializamos colorama para mejorar la interfaz en la terminal
init(autoreset=True)

#CREA LA BASE DE DATOS
def crear_db_tabla():
    """crear la db inventario y la tabla productos"""
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT)""")
    conn.commit()
    conn.close()

#CONEXION CON LA BASE DE DATOS
def conexion_db():
    """retorna la conexion y el cursor"""
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    return conn, cursor

#funcion superior que recibe como parametro las funciones (registrar, actualizar y eliminar productos) y una o varias variables
def consultas_db(func_consulta, *args):
    """funcion padre(recibe funcion,argumentos y retorna mensaje o datos)"""
    conn, cursor = conexion_db()
    try:
        resultado = func_consulta(cursor, *args)
        conn.commit()
        return resultado
    except ConnectionError:
        conn.rollback()
        print(Fore.RED + "Error, conexion con la db fallo")
    finally:
        conn.close()

#INGRESAR NUEVO PRODUCTO
def registrar_producto(cursor):
    nombre, descripcion, cantidad, precio, categoria = ingreso_datos()
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES(?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))
    print(Fore.GREEN + "Producto Ingresado Correctamente\n")


def listar_productos(cursor):
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()

def listar_producto(cursor, id_producto):
    cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
    return cursor.fetchone()

def listar_bajo_stock(cursor, stock):
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (stock, ))
    return cursor.fetchall()

#CONSULTAR PRODUCTO SEGUN FUNCION RECIBIDA(LISTAR_PRODUCTO - LISTAR_PRODUCTOS - LISTAR_BAJO_STOCK)
def consultar_productos(func_consulta):
    if func_consulta == listar_producto:
        id_prod = input("Ingrese el ID del producto: ")
        productos = consultas_db(func_consulta, id_prod) #--> tupla()
    elif func_consulta == listar_productos:
        productos = consultas_db(func_consulta) #--> lista[]
    elif func_consulta == listar_bajo_stock:
        stock = int(input("Ingrese el stock maximo a buscar: "))
        productos = consultas_db(func_consulta, stock) #--> lista[]
    if productos:
        # Definir el formato de la tabla
        print(Fore.LIGHTBLUE_EX + "+----+----------------------+--------------------------+----------+-----------+--------------------------+")
        print(Fore.LIGHTBLUE_EX + "| ID | Nombre               | Descripción              | Cantidad |   Precio  | Categoría                |")
        print(Fore.LIGHTBLUE_EX + "+----+----------------------+--------------------------+----------+-----------+--------------------------+")
        
        if isinstance(productos, list):
            for producto in productos:
                id_col = str(producto[0]).ljust(2)[:2]#--> solo 2 caracteres
                nombre_col = str(producto[1]).ljust(20)[:20]
                descripcion_col = str(producto[2]).ljust(24)[:24]
                cantidad_col = str(producto[3]).rjust(8)[:8]
                precio_col = f"${producto[4]:.2f}".rjust(9)[:9]
                categoria_col = str(producto[5]).ljust(24)[:24]
                print(f"| {id_col} | {nombre_col} | {descripcion_col} | {cantidad_col} | {precio_col} | {categoria_col} |")
        else:
            id_col = str(productos[0]).ljust(2)[:2]
            nombre_col = str(productos[1]).ljust(20)[:20]
            descripcion_col = str(productos[2]).ljust(24)[:24]
            cantidad_col = str(productos[3]).rjust(8)[:8]
            precio_col = f"${productos[4]:.2f}".rjust(9)[:9]
            categoria_col = str(productos[5]).ljust(24)[:24]
            print(f"| {id_col} | {nombre_col} | {descripcion_col} | {cantidad_col} | {precio_col} | {categoria_col} |")
            
        print(Fore.LIGHTBLUE_EX + "+----+----------------------+--------------------------+----------+-----------+--------------------------+")
        print("")
    else:
        print(Fore.RED + "Lista de productos vacia.")
        print("")

#ACTUALIZAR PRODUCTO PRO ID
def actualizar_producto(cursor):
    try:
        id = int(input("Ingrese el Id del producto a actualizar: "))
        
        if(consultas_db(listar_producto, id)):
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            cursor.execute("UPDATE productos SET cantidad = ? WHERE id_producto = ?", (cantidad, id))
            print(Fore.GREEN + "Producto Actualizado Correctamente\n")
        else:
            print(Fore.RED + f"El producto no existe\n")
    
    except ValueError:
        print(Fore.RED + "Los datos ingresados son incorrectos")
    
#ELIMINAR PRODUCTO POR ID
def eliminar_producto(cursor):
    try:
        id = int(input("Id del producto a eliminar: "))
        if(consultas_db(listar_producto, id)):
            cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id,))
            print(Fore.GREEN + "Producto Eliminado con Exito\n")
        else:
            print(Fore.RED + f"El producto no existe\n")
    except ValueError:
        print(Fore.RED + "Los datos ingresados son incorrectos")


def ingreso_datos():
    """validar ingreso de datos mediante while y try-except"""
    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese una breve descripcion del producto: ")
            if descripcion in ['', None]:
                descripcion = "Producto sin descripcion"
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: $"))
            categoria = input("Ingrese la categoria a la cual pertenece el producto: ")
            if categoria in ['', None]:
                categoria = "Producto sin categoria"
            return nombre, descripcion, cantidad, precio, categoria
        
        except ValueError:
            print(Fore.RED + "Los datos ingresados son incorrectos")
            continue


opciones_lista = []
#Menú interactivo
def menu():
    crear_db_tabla()#DB-->inventario.db - Table-->Productos
    
    while True:
        print(Back.BLUE + Style.BRIGHT + "Menú de opciones:")
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "1." + Style.RESET_ALL + " Registrar producto")
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "2." + Style.RESET_ALL + " Consultar producto")
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "3." + Style.RESET_ALL + " Actualizar producto")
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "4." + Style.RESET_ALL + " Eliminar producto")
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "5." + Style.RESET_ALL + " Listar productos")
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "6." + Style.RESET_ALL + " Reporte de bajo stock")
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "7." + Fore.LIGHTRED_EX+ " Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            consultas_db(registrar_producto)
        elif opcion == "2":
            consultar_productos(listar_producto)
        elif opcion == "3":
            consultas_db(actualizar_producto)
        elif opcion == "4":
            consultas_db(eliminar_producto)
        elif opcion == "5":
            consultar_productos(listar_productos)
        elif opcion == "6":
            consultar_productos(listar_bajo_stock)
        elif opcion == "7":
            print(Fore.BLACK + "Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.\n")
            

############################################################
#Ejecutar el menú
if __name__ == "__main__":
    menu()