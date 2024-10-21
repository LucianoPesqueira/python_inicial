ventas = []
seguir = "S"

#registrar venta mientras no escriba S
while seguir == "S":
    producto = input("Ingresa el nombre del producto: ")
    ventas.append(producto)

    seguir = input("Queres seguir? (S/N)").upper()


#mostrar producto

print("\nProductos vendidos hoy:")
indice = 0

while indice < len(ventas):
    print(f"Producto {indice + 1}: {ventas[indice]}")
    indice += 1