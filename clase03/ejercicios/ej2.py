"""Escribe un programa en Python que calcule la
propina que se debe dejar en un restaurante.

El script debe solicitar al usuario el monto total de
la cuenta y el porcentaje de propina que desea
dejar.

Utilizando operadores aritméticos, calcula la
cantidad de propina y el total a pagar (incluyendo
la propina).

Finalmente, muestra los resultados en la pantalla.
"""

cuenta = float(input("Ingrese el monto total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje(%) de propina que desea dejar: "))

propina = (cuenta * porcentaje_propina) / 100
cuenta_total = cuenta + propina

print(f"la propina es: ${propina:.0f}")
print(f"El total a pagar entre el monto de la cuenta y la propina es: ${cuenta_total}")
