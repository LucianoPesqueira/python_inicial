"""Gestión de descuentos

Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. Vas a desarrollar un programa que permita
calcular el precio final de un producto después de aplicar un descuento. Para hacerlo:

Crea una función que reciba como parámetros el precio original del producto y el porcentaje de descuento, y que retorne
el precio final con el descuento aplicado.

Luego, pedí que se ingrese el precio y el porcentaje de descuento. Mostrá el precio final después de aplicar el descuento."""

def precio_final(precio_original, descuento):
    return precio_original - (precio_original * descuento / 100)


precio = float(input("Ingrese el precio del producto: "))
descuento = int(input("Ingrese el descuento a aplicar: "))

print(f"El precio final con el descuento es: {precio_final(precio, descuento)}")