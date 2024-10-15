"""Validación de precios de productos

Escribí un programa que permita al usuario ingresar el precio de un producto, pero que sólo acepte valores
mayores a 0. Si el usuario ingresa un valor inválido (negativo o cero), el programa debe mostrar un mensaje de
error, y volver a pedir el valor hasta que se ingrese uno válido. Al final, el programa debe mostrar el precio
aceptado.

Tips:

Antes de empezar, pensá si es necesario usar contadores o acumuladores.

Recordá que input() siempre devuelve cadenas de caracteres.
"""

precio = float(input("ingrese el precio del producto: "))

while precio <= 0:
    print("Error. debe ser mayor a cero(0)")
    precio = float(input("ingrese el precio del producto: "))

print(f"precio aceptado: {precio}")


