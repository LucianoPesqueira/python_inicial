"""Control de inventario de una tienda de videojuegos

Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. El dueño te pide que
escribas un programa que verifique si hay stock suficiente de un videojuego y, si no hay, que avise que hay
que reponerlo.

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad,
mostrar si se necesita hacer un nuevo pedido o no."""

stock_actual = int(input("ingrese el stock actual del videojuego: "))

if stock_actual <= 0:
    print("requiere realizar un pedido nuevo del producto")
elif stock_actual < 10:
    print("stock bajo, podria realizar un pedido nuevo")
else:
    print("el stock es el correcto")