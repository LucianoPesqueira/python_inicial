import sqlite3


def crear_db_tabla():
    """crear la db y la tabla productos"""
    conn = sqlite3.connect("clase15--09-12/producto_ejemplo.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL)""")
    conn.commit()
    conn.close()

def conexion_db():
    conn = sqlite3.connect("clase15--09-12/producto_ejemplo.db")
    cursor = conn.cursor()
    return conn, cursor

def consultas_db(func_consulta, *args):
    conn, cursor = conexion_db()
    
    try:
        resultado = func_consulta(cursor, *args)
        conn.commit()
        return resultado
    except ConnectionError:
        conn.rollback()
        print("Error, conexion con la db fallo")
    finally:
        conn.close()


def registrar_producto(cursor, nombre, precio, cantidad):
    cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES(?, ?, ?)", (nombre, precio, cantidad))
    return "Producto Ingresado Correctamente"



def listar_productos(cursor):
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()

def listar_producto(cursor, nombre):
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    return cursor.fetchone()

def consultar_productos(func_consulta):
    #productos = consultas_db(listar_productos)
    if func_consulta == listar_producto:
        nombre = input("Ingrese el nombre del producto: ")
        productos = consultas_db(func_consulta, nombre) #--> tupla()
    elif func_consulta == listar_productos:
        productos = consultas_db(func_consulta) #--> lista[]
    elif func_consulta == listar_bajo_stock:
        stock = int(input("Ingrese el stock maximo a buscar: "))
        productos = consultas_db(func_consulta, stock) #--> lista[]
    print("\n  *** Lista de productos ***")
    if productos:
        if isinstance(productos, list):
            for producto in productos:
                print(f"Id: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]:.2f}, Cantidad: {producto[3]}")
            print("")
        else:
            print(f"Id: {productos[0]}, Nombre: {productos[1]}, Precio: {productos[2]:.2f}, Cantidad: {productos[3]}")
            print("")
    else:
        print("Lista de productos vacia.")



#LISTA DE UN SOLO PRODUCTO
#PRODUCTO
# def listar_producto(cursor, nombre):
#     cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
#     return cursor.fetchone()

# def consultar_producto():
#     nombre = input("Ingrese el nombre del producto: ")
#     producto = consultas_db(listar_producto, nombre)
#     print("Producto buscado")
#     if producto:
#         print(f"Id: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]:.2f}, Cantidad: {producto[3]}")
#     else:
#         print("Producto no encontrado!")
#END PRODUCTO

def actualizar_producto(cursor):
    id = int(input("Ingrese el Id del producto a actualizar: "))
    nombre, precio, cantidad = ingreso_datos()
    cursor.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ? WHERE id_producto = ?", (nombre, precio, cantidad, id))
    return "Producto Actualizado Correctamente"

def eliminar_producto(cursor):
    id = int(input("Id del producto a eliminar: "))
    cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id,))
    return "Producto Eliminado con Exito"

def listar_bajo_stock(cursor, stock):
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (stock, ))
    return cursor.fetchall()

def ingreso_datos():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: $"))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    return nombre, precio, cantidad


#Menú interactivo
def menu():
    crear_db_tabla()
    
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
            nombre, precio, cantidad = ingreso_datos()
            print(consultas_db(registrar_producto, nombre, precio, cantidad)) #--> Producto Ingresado Correctamente
        elif opcion == "2":
            #print(consultas_db(consultar_productos))#--> []
            consultar_productos(listar_producto)
        elif opcion == "3":
            print(consultas_db(actualizar_producto))
        elif opcion == "4":
            print(consultas_db(eliminar_producto))
        elif opcion == "5":
            consultar_productos(listar_productos)
        elif opcion == "6":
            consultar_productos(listar_bajo_stock)
        elif opcion == "7":
            print("Saliendo del programa, chau chau...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
            

#Ejecutar el menú
if __name__ == "__main__":
    menu()


##################################################################################################################3
# import sqlite3

# # Función superior para manejar consultas a la base de datos
# def consultas_db(query_func, *args, **kwargs):
#     cursor, conn = conexion_db()
#     try:
#         # Ejecuta la función pasada como parámetro
#         resultado = query_func(cursor, *args, **kwargs)
#         conn.commit()
#         return resultado
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         conn.close()

# # Función que realiza una consulta específica
# def obtener_usuarios(cursor):
#     """Ejecuta una consulta para obtener todos los usuarios."""
#     cursor.execute("SELECT * FROM usuarios")
#     return cursor.fetchall()

# # Función que inserta un nuevo usuario
# def insertar_usuario(cursor, nombre, edad):
#     """Ejecuta una consulta para insertar un nuevo usuario."""
#     cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))

# # Uso de la función superior
# if __name__ == "__main__":
    
#     # Insertar un usuario
#     consultas_db(insertar_usuario, "Luciano", 30)
    
#     # Obtener usuarios
#     usuarios = consultas_db(obtener_usuarios)
#     print(usuarios)
