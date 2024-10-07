"""
Crea un programa que solicite al usuario dos
números enteros.

Realiza las siguientes operaciones: suma,
resta, multiplicación, y módulo.

Muestra el resultado de cada operación en un
formato claro y amigable.

Asegúrate de incluir mensajes personalizados que
expliquen cada resultado, por ejemplo: "La suma
de tus números es: X".
"""

num1 = float(input("Ingrese un numero: ")) 
num2 = float(input("Ingrese otro numero: "))

print(f"La suma es: {num1 + num2}")
print(f"La resta es: {num1 - num2}")
print(f"La multiplicacion es: {num1 * num2}")
print(f"El modulo es: {num1 % num2}")