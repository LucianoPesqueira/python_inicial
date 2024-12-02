"""Simulación de precios con math y random

Supongamos que deseás simular los precios de 10 productos en un
inventario. Escribí un programa que:

    Utilice el módulo random para generar 10 precios aleatorios
    entre $10.00 y $100.00.

    Redondee los precios generados a dos decimales usando una
    función del módulo math."""
import random, math
def simular_precios_inventario():
    precios = random.uniform(10.00, 100.00)
    
    redondeo = math.floor(precios * 100) / 100
    
    return redondeo

precios = []

for i in range(10):
    precio = simular_precios_inventario()
    precios.append(precio)
    print(f"Precio producto {i + 1}: {precio}")