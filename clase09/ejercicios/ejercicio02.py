"""en un sistema de inventario, cada producto tiene un codigo que lo identifica.
Escribi un programa que permita ingresar los codigos de 4 productos y luego mostrarlos uno por uno, junto con su posicion en la lista
ejem: si los codigos ingresados son "P001", "P002", "P003", "P004" el programa debe mostrar:
Producto 1: P001
Producto 2: P002
Producto 3: P003
Producto 4: P004

tips utiliza un bucle for y range() para recorrer los codigos e imprimirlos
"""

productos = []

for i in range(4):
    code = input("Ingrese el codigo del producto " + str(i + 1) + ": ")

    productos.append(code)


for i in range(len(productos)):
     print(f"Producto {i + 1}: {productos[i]}")