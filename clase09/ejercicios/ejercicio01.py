"""desarrolla una funcion que calcule la suma de los n naturales hasta un numero dado utilizando un buble for.
la suma de los n naturales hasta el num n se define como la suma de todos los num enteros positivos desde 1 a n.
ej: suma num nat hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21"""

num = int(input("ingrese un numero entero positivo: "))

while num <= 0:
    print("debe ser mayor que cero")
    num = int(input("ingrese un numero entero positivo: "))

sum = 0

for n in range(1, num + 1):
    print(n)
    sum += n

print(f"la suma de num naturales hasta {num} es: {sum}")