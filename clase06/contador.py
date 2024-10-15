intentos = 0

cantidad = int(input("Ingresa la cantidad de productos: "))

while cantidad <= 10:
    intentos += 1
    print("Error: la cantidad debe ser mayor a cero")

    cantidad = int(input("Ingresa la cantidad de productos: "))

print(f"cantidad de intentos: {intentos}")