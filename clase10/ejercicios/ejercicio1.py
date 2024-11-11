"""
En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa que permita:

Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un diccionario donde
la clave es el nombre del producto y el valor es su precio.

Una vez ingresados, mostrará todos los productos y sus precios en pantalla.
            Producto: Manzanas, Precio: 100

            Producto: Naranjas, Precio: 150

            Producto: Peras, Precio: 120
"""

productos = {}

for i in range(3):
    nombre = input(f"Nombre del producto {i+1}: ")
    precio = float(input("Precio del producto: "))
    productos[nombre] = precio

for nombre, precio in productos.items():
    print(f"Producto: {nombre},  Precio: ${precio:.2f}")