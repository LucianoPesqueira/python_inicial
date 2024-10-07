personas = int(input("Ingrese la cantidad de personas que van a cenar: "))
precio_plato = float(input("ingrese el precio del plato: $"))

total_cena = personas * precio_plato
propina = total_cena * 0.10
total = total_cena + propina

print("Datos de la cena")
print("----------------")
print(f"Total de la cena: $ {total_cena} / propina: $ {propina}")
print(f"Total a pagar: $ {total}")