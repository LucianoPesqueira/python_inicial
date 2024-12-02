#funciones
def saludar(): #definicion de una funcion
    print("Hola", "¡Bienvenido!")
    

# Diccionario “inventario”:

inventario = {
1: {"nombre": "Manzana", "descripcion": "Fruta fresca",

    "cantidad": 50, "precio": 0.5, "categoria": "Frutas"},

2: {"nombre": "Pan", "descripcion": "Pan casero",

    "cantidad": 20, "precio": 1.0, "categoria": "Panadería"}
}

#Registro de productos
inventario = {}
codigo_actual = 1

def registrar_producto():
    global codigo_actual
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    #agregar el producto al diccionario
    inventario[codigo_actual] = {
        "nombre" : nombre,
        "descripcion" : descripcion,
        "cantidad" : cantidad,
        "precio" : precio
    }
    
    print(f"Producto registrado con el codigo {codigo_actual}")
    codigo_actual += 1
    

#listado de productos
#si esta vacio --> informar vacio
#recorre el dict con for 


#actualizar productos
#cuando se requiere actualizar el stock o el precio
#ingrese el codigo de producto --> producto actualizado


#eliminacion de producto
#se elimina en base al codigo del producto
#buscar en base al codigo
#si no esta --> informar


#busqueda de producto
#en base al codigo del producto


#reporte stock bajo
#en base a un stock ingresado --> muestre los productos con ese stock o inferior al mismo
#valores logicos a ingresar


#menu principal
#puede ser un funcion --> menu principal()
