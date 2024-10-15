"""Control de stock de productos

Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock
que hay de cada uno. El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida
salir, ingresando "salir" como nombre de producto. Después de que el bucle termine, el programa debe mostrar
la cantidad total de productos ingresados.

Tips:

Vas a necesitar un contador.

Tené presente las estructuras condicionales.
"""

producto =  ""
stock = 0
stock_total = 0

while producto != "salir":
    producto = input("Nombre del producto: ")

    if producto != "salir":
        #stock = int(input("ingrese el stock: "))
        str_stock = input("ingrese el stock: ")
        if str_stock.isdigit():
            stock = int(str_stock)
            stock_total += stock
        else:
            break


print(f"stock total es: {stock_total}")

