total_productos = 0

for dia in range(3):
     print(f"dia: {dia + 1}: ")
     productos_agregados = int(input("Productos ingresados en el dia: "))
     total_productos += productos_agregados

print(f"Se ingresaron: {total_productos}")