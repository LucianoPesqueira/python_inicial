#
dias = 5
ventas_dias = []
total_ventas = 0


dia = 1
while dia <= dias:
    try:
        venta = float(input(f"Ingresar el monto de las ventas del dia {dia}: "))
        if venta >= 0:
            ventas_dias.append(venta)
            total_ventas += venta
            dia += 1
        else:
            print("El monto debe ser un valor mayor a 0. Intente de nuevo!")
    except ValueError:
        print("Error: debe ingresar un valor valido")

print("Resumen de ventas diarias:")
for i, venta in enumerate(ventas_dias, 1):
    print(f"Dia {i}: $ {venta:.2f}")

promedio_ventas = total_ventas / dias
print(f"Total de ventas: $ {total_ventas:.2f}")
print(f"Promedio de ventas: $ {promedio_ventas:.2f}")
