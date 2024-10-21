productos = ["lapiz", "cuaderno", "hojas", "tijera"]

#consultar productos en el inventario

consulta = input("Ingresa el nombre del producto a consultar: ")

#verifico si el producto se encuentra en el inventario
indice = 0
encontrado = False

while indice < len(productos):
    if productos[indice] == consulta:
        encontrado = True
        break
    indice += 1

if encontrado:
    print(f"El producto {consulta}, se encuentra en el inventario")
else:
    print("producto no disponible")