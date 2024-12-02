"""Cálculo de promedio de ventas

Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

Creá una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas ventas.

Solicitá a la persona que ingrese las ventas de cada día durante una semana (7 días). Usá la función para calcular y
mostrar el promedio de ventas al finalizar."""

def promedio(ventas):
    return (sum(ventas) / len(ventas))


ventas = []
for i in range(7):
    ventas.append(float(input(f"Ingrese la venta del dia {i + 1}: ")))
    
print(f"El promedio de las ventas de una semana es: {promedio(ventas)}")