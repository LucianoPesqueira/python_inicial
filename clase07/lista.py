compras = ["manzanas", "quesos", "naranjas", "tomates"]
compras[1] = "yogur"
compras.append("cebollas")
compras.remove("tomates")

indice = 0

while indice < len(compras):
    print(f"Producto {indice + 1}: {compras[indice]}")
    indice += 1

print(compras)