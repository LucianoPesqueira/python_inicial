def cuadrado(n):
    return n * n

resultado = cuadrado(7)
print(f"El cuadrado de 7 es {resultado}")




######################otro ejemplo####################################
def calcular_total(precio, cantidad):
    return precio * cantidad

total_veces = calcular_total(100, 3)
print(f"El total de las ventas es: {total_veces}")


##############################################################
#funcion que calcule las ventas de un producto

def calcular_ventas_productos():
    ventas = 10
    return ventas

def calcular_ventas_productos2():
    ventas = 15
    return ventas

def calcular_ventas_totales():
    total = calcular_ventas_productos() + calcular_ventas_productos2()
    return total

ventas_totales = calcular_ventas_totales()
print(ventas_totales)
