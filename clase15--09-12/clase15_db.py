#bases de datos

#importar el modulo
import sqlite3 # Importar el módulo

#MENU OPCION 2:
##ERRORES:
"""
TENGO QUE CAMBIAR LA CONEXION A LA DB DE TODAS LAS FUNCIONES PARA QUE APUNTE A clase15--09-12/productos.db
PUEDO CREAR UNA FUNCION PARA CONECTAR LA DB Y LUEGO LLAMARLA DESDE CADA FUNCION DEL CRUD
PUEDO CREAR UNA FUNCION QUE DEFINA LA CONEXION Y CREAR CADA UNA DE LAS CONSULTAS RECIBIENDO COMO PARAMETRO LOS DATOS A UTILIZAR
"""

def inicializar_db():
    conn = sqlite3.connect("clase15--09-12/productos.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id_product INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT NOT NULL,
        price_product REAL NOT NULL,
        qty_product INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    
#registrar producto
def registrar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: $"))
    cantidad = int(input("Cantidad del producto: "))
    
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (name_product, price_product, qty_product) VALUES(?, ?, ?)", (nombre, precio, cantidad))
    
    conn.commit()
    conn.close()

#consultar_producto
def consultar_producto():
    id_producto = int(input("Id del producto a buscar: "))
    
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id_product = ?", (id_producto))
    resultados = cursor.fetchone()

    if resultados:
        for registro in resultados:
            print(f"Nombre:, {registro[0]}, Precio: $, {registro[1]:.2f}, Cantidad:, {registro[2]}")
    else:
        print("Error, producto no encontrado")
    conn.close()
    
#actualizar producto
def actualizar_producto():
    id_producto = int(input("Id del producto a buscar: "))
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: $"))
    cantidad = int(input("Cantidad del producto: "))
    
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ? WHERE id_product = ?", (id_producto, nombre, precio, cantidad))
    
    conn.commit()
    conn.close()
    print("actualizado")
    
#eliminar un producto
def eliminar_producto():
    id_producto = int(input("Id del producto a buscar: "))
    
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto))
    
    conn.commit()
    conn.close()
    print("eliminado")
    
    
#lista de productos
def lista_productos():
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    if productos:
        print("lista de productos: ")
        for prod in productos:
            print(f"id:{prod[0]}, nombre:{prod[1]}, precio:{prod[2]}, cantidad:{prod[3]}")
            
            
#mostrar bajo stock
def productos_bajo_stock():
    limite = int(input("ingrese el stock a buscar: "))
    
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE qty_product <= ?", (limite))
    productos = cursor.fetchall()
    conn.close()
    if productos:
        print("lista de productos con bajo stock: ")
        for prod in productos:
            print(f"id:{prod[0]}, nombre:{prod[1]}, precio:{prod[2]}, cantidad:{prod[3]}")
    else:
        print("no hay productos")
        
        

#Menú interactivo
def menu():
    inicializar_db()
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
            lista_productos()
        elif opcion == "6":
            productos_bajo_stock()
        elif opcion == "7":
            print("Saliendo del programa, chau chau...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

#Ejecutar el menú
if __name__ == "__main__":
    menu()