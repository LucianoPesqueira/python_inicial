"""
Escribir un programa que solicite el nombre, la
cantidad y el valor unitario de tres productos.

Luego, debe calcular el importe de IVA (21%)
de cada producto.

Por último, debe mostrar en la terminal el
ticket de la operación con todos los datos de la
compra."""

nombre_prod1 = input("ingrese el nombre del primer producto: ")
cant_prod1 = int(input("ingrese la cantidad: "))
val_prod1 = float(input("ingrese el valor unitario del producto: $"))

nombre_prod2 = input("\ningrese el nombre del segundo producto: ")
cant_prod2 = int(input("ingrese la cantidad: "))
val_prod2 = float(input("ingrese el valor unitario del producto: $"))

nombre_prod3 = input("\ningrese el nombre del tercer producto: ")
cant_prod3 = int(input("ingrese la cantidad: "))
val_prod3 = float(input("ingrese el valor unitario del producto: $"))

#cantidad * precio unitario
precio_prod1 = cant_prod1 * val_prod1
precio_prod2 = cant_prod2 * val_prod2
precio_prod3 = cant_prod3 * val_prod3

#importe de IVA (21%)
iva_prod1 = precio_prod1* 0.21
iva_prod2 = precio_prod2 * 0.21
iva_prod3 = precio_prod3 * 0.21

#total con IVA (21%)
total_prod1 = precio_prod1 + iva_prod1
total_prod2 = precio_prod2 + iva_prod2
total_prod3 = precio_prod3 + iva_prod3

#mostrar ticket
print("\n--- TICKET COMPRA ---")
print("\nproducto 1:")
print(f"Nombre: {nombre_prod1}, cantidad: {cant_prod1}, valor unitario: ${val_prod1}")
print(f"Precio Total: ${precio_prod1}")
print(f"importe de IVA: ${iva_prod1}")
print(f"Total con IVA: ${total_prod1}")

print("\nproducto 2:")
print(f"Nombre: {nombre_prod2}, cantidad: {cant_prod2}, valor unitario: ${val_prod2}")
print(f"Precio Total: ${precio_prod2}")
print(f"importe de IVA: ${iva_prod2}")
print(f"Total con IVA: ${total_prod2}")

print("nproducto 3:")
print(f"Nombre: {nombre_prod3}, cantidad: {cant_prod3}, valor unitario: ${val_prod3}")
print(f"Precio Total: ${precio_prod3}")
print(f"importe de IVA: ${iva_prod3}")
print(f"Total con IVA: ${total_prod3}")