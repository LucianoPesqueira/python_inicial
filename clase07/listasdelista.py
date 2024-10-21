#lista de productos: nombre, precio y cantidad

inventario = [
    ["manzanas", 100, 50],
    ["pan", 35, 20],
    ["leche", 55, 120]
]

#modificar un producto

producto_modificar = input("Que producto quiere modificar?: ")

indice = 0
while indice < len(inventario):
    if inventario[indice][0] == producto_modificar:
        #precio
        resp = input("desea cambiar el precio?:(s/n) ").upper()
        if resp == "S":
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            inventario[indice][1] = nuevo_precio
        #cantidad
        resp = input("desea cambiar la cantidad?:(s/n) ").upper()
        if resp == "S":
            nueva_cantidad = input("Ingrese la nueva cantidad: ")
            inventario[indice][2] = nueva_cantidad  
        break
    indice += 1


#mostrar el inventario actualizado
print("\nInventario actualizado:")

indice = 0

while indice < len(inventario):
    producto = inventario[indice]
    print(f"producto: {producto[0]}")
    print(f"Precio: ${producto[1]}")
    print(f"cantidad: {producto[2]}")
    print("-----------------------------")
    indice += 1