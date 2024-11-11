productos = {
    "Manzanas": 50,
    "Peras": 30,
    "Bananas": 40
}
print(productos["Peras"])

#get()
print(productos.get("Bananas", 0))#defino valor por defecto es 0
print(productos.get("Uvas"))#sin definir, valor por defecto es None

#agregar a dict
productos["Naranjas"] = 35
print(productos)

#eliminar con del
del productos["Peras"]
print(productos)

#eliminar los datos de un dict con clear()
productos2 = productos.copy()
print(productos2)
productos2.clear()
print(productos2)

#recorrer un dict con items()
print("Nombre\t\tvalor")
for key,value in productos.items():
    print(f"{key} \t{value}")

#keys y values()
for key in productos.keys():
    print("Productos:", key)

for value in productos.values():
    print("los valores:", value)