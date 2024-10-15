cantidad = int(input("Ingrese la cantidad de productos: "))

while cantidad <= 0:
    print("Debe ser mayor a 0 (cero)")
    cantidad = int(input("Ingrese la cantidad de productos: "))

print(f"La cantidad ingresada es: {cantidad}")