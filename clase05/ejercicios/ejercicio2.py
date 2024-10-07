"""Compra con descuentos

Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de
artículos que está comprando. El programa debe determinar el descuento aplicable según las siguientes
reglas:

Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000,
aplica un descuento del 15%.

Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento
del 10%.

Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.

Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier
descuento o simplemente el monto original si no hay descuento."""


monto_total = float(input("ingrese el monto total de la compra: $"))
articulos_total = int(input("ingrese la cantidad de articulos: "))

if articulos_total >= 5 and monto_total > 10000:
    print("se aplicara un descuento del 15%")
    total = monto_total - (monto_total * 0.15)
    print(f"${total}")
elif articulos_total < 5 and articulos_total >=3:
    print("se aplicara un descuento del 10%")
    total = monto_total - (monto_total * 0.10)
    print(f"${total}")
else:
    print("sin descuentos")
    print(f"${monto_total}")

