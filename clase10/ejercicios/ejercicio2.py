"""
El inventario de una tienda está almacenado en un diccionario, donde las claves son los nombres de los
productos y los valores son las cantidades disponibles en stock. Creá un programa que:

Te permita ingresar el nombre de un producto.

Utilice el método .get() para buscar el stock disponible. Si el producto no existe, deberá mostrar un
mensaje diciendo "Producto no encontrado".

Si el producto está disponible, mostrará cuántas unidades quedan en stock.

Diccionario inicial:
productos = {
"Manzanas": 50,
"Naranjas": 30,
"Peras": 25
}
salida:
Ingresá el nombre del producto: Peras
Stock disponible de Peras: 25
"""

productos = {
"Manzanas": 50,
"Naranjas": 30,
"Peras": 25
}
nombre = input("Ingrese el nombre del producto a buscar: ")
stock = productos.get(nombre)
if stock is not None:
    print(f"Stock disponible de {nombre}: {stock}")
else:
    print("Producto no encontrado")