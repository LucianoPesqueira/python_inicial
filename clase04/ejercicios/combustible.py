"""
Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que
consume un coche por cada 100 km de recorrido,
el costo de cada litro de combustible y la longitud
del viaje realizado (en kilómetros), muestra un
detalle de los litros consumidos y el dinero
gastado."""

litros_100 = float(input("Ingrese la cantidad de litros que consume por c/100KM: "))
costo_litro = float(input("Costo de cada litro: "))
long_viaje = float(input("longitud de viaje en KM: "))

#litros consumidos
litro_consumo = (litros_100 * long_viaje) / 100

#costo 
costo = litro_consumo * costo_litro

#print
print("Litros de combustible consumidos: ", litro_consumo)
print("dinero gastado: $", costo)

