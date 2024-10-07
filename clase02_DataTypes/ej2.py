# Escribir un programa que guarde en variables el
# monto del ingreso de cada uno de los primeros 6
# meses del año.

# Luego, calcular y guardar en otra variable el
# promedio de esos valores.

# Por último, mostrar una leyenda que diga “El
# ingreso promedio en el semestre es de xxxxx”
# donde “xxxxx” es el valor calculado.

enero = 24000
febrero = 12000
marzo = 35000
abril = 50000
mayo = 25000
junio = 10900

prom = (enero + febrero + marzo + abril + mayo + junio) / 6

print(f"El promedio del ingreso del semestre es: {prom}")