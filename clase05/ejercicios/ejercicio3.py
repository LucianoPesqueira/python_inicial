nota1 = int(input("nota1: "))
nota2 = int(input("nota2: "))
nota3 = int(input("nota3: "))
nota4 = int(input("nota4: "))

prom = (nota1 + nota2 + nota3 + nota4) / 4

if prom >=9:
    print("Excelente nota!!")
elif prom >= 7:
    print("buena nota!!!")
elif prom >= 6:
    print("aprobaste!!")
else:
    print("desaprobaste!!")
print(f"promedio: {prom}")