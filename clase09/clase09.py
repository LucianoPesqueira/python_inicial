#FOR
#lista
productos = ["lapices", "hojas", "gomas", "carpetas"]
print("lista")
for p in productos:
    print(p)

#cadena
palabra = "Python"
print("\ncadena:")
for letra in palabra:
    print(letra)

#tupla
numeros = (1, 4, 76, 8, 5)
print("\nTupla:")
for n in numeros:
    print(n)

#for anidado
frutas = ["manzana", "banana", "pera"]
print("\nanidado:")
for fruta in frutas:
    print("fruta:", fruta)
    for letra in fruta:
        print("letra:", letra)

#lista de productos
productos = ["P001", "P002", "P003", "P004", "P005"]

#producto a buscar
productos_buscar = "P005"

for producto in productos:
    if producto == productos_buscar:
        print("Producto encontrado:", producto)
        break #detiene la ejecucion

#range
for i in range(10, 0, -2): #(0, 10, 3)--> 0 3 6 9
    print(i)

