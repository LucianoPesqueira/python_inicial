inventario = {
    "Manzanas": 50,
    "Peras": 30,
    "Bananas": 40
}

ventas_dia = {}

for _ in range(3):
    producto = input("ingrese el producto vendido: ")
    cantidad_vendida = int(input("cantidad vendida: "))

    if producto in inventario:
        ventas_dia[producto] = cantidad_vendida
    else:
        print("producto no encontrado")

for producto,cantidad in ventas_dia.items():
    inventario[producto] = inventario[producto] - cantidad

print(inventario)