edad = 5

if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

edad2 = 20

tiene_licencia = True

if edad2 >= 18:
    if tiene_licencia:
        print("puede conducir")
    else:
        print("no puede conducir por falta de licencia")
else:
    print("no tiene la edad para conducir")