"""Generación de valores únicos con random

Escribí un programa en Python que genere cinco códigos únicos de
cinco dígitos para usarlos como identificadores de productos en un
inventario. Para esto, utilizá el módulo random. Cada código
generado debe ser diferente de los otros.

Tip: Podés usar random.randint() para generar números dentro de un
rango determinado."""

import random

def generar_codigos_unicos(cantidad, longitud):
    codigo = set()
    while len(codigo) < cantidad:
        codigo_generado = random.randint(10**(longitud-1), 10**longitud-1)
        codigo.add(codigo_generado)
    return list(codigo)

cantidad_cod = 5
longitud_cod = 5
codigo = generar_codigos_unicos(cantidad_cod, longitud_cod)

print(codigo) #--> [77285, 74537, 54956, 99730, 33587]