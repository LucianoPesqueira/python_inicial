"""actualizacion de inventario a partir de un arreglo
-seleccionar un producto a partir de su codigo
-ingresar la cantidad vendida(que debe ser mayor a cero)
-actualizar la cantidad en stock de ese producto restando la cantidad vendida

el arreglo:
productos = {
    ["P001", "manzana", 50],
    ["P002", "peras", 40],
    ["P003", "bananas", 30],
    ["P004", "naranjas", 60]
}"""

productos = [
    ["P001", "Manzana", 50],
    ["P002", "Peras", 40],
    ["P003", "Bananas", 30],
    ["P004", "Naranjas", 60]
]


#mostrar
for p in productos:
    print(f"{p[0]}",
          f"{p[1]}",
          f"{p[2]}")

#mostrar por codigo
codigo = input("ingrese el codigo del producto vendido: ")

encontrado = False
for producto in productos:
    if producto[0] == codigo:
        cantidad_vendida = int(input("ingrese la cantidad vendida: "))
        while cantidad_vendida <= 0:
            print("cantidad debe ser mayor a 0")
            cantidad_vendida = int(input("ingrese la cantidad vendida: "))
        if cantidad_vendida > producto[2]:
            print("Error, no hay suficiente stock")
        else:
            producto[2] = producto[2] - cantidad_vendida
            print("venta realizada, el nuevo stock de", producto[1], "es", producto[2])