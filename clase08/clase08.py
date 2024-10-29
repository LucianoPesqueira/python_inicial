producto = []
cantidad = []
precio = []

while True:
    print("---------Menu Principal-----------")
    print("1-Agregar Producto")
    print("2-Modificar Producto")
    print("3-Buscar Producto")
    print("4-Ver Producto")
    print("5-Salir")

    opc = input("Ingrese una opcion 1-5: ")
    #AGREGAR PRODUCTO
    if opc == "1": 
        prod_name = input("Ingrese el nombre del producto: ")
        prod_cant = input("Ingrese la cantidad: ")
        prod_prec = input("Ingrese el precio: ")

        producto.append(prod_name)
        cantidad.append(prod_cant)
        precio.append(prod_prec)
    #MODIFICAR PRODUCTO
    elif opc == "2":
        buscar = input("Nombre del producto a modificar: ")
        posicion = producto.index(buscar)

        prod_name = input("Ingrese el nombre del producto: ")
        prod_cant = input("Ingrese la cantidad: ")
        prod_prec = input("Ingrese el precio")

        producto[posicion] = prod_name
        cantidad[posicion] = prod_cant
        precio[posicion] = prod_prec
    #BUSCAR PRODUCTO
    elif opc == "3":
        buscar = input("Nombre del producto a buscar: ")
        posicion = producto.index(buscar)

        print(f"El nombre del producto es: {producto[posicion]}")
        print(f"La cantidad del producto es: {cantidad[posicion]}")
        print(f"El precio del producto es: {precio[posicion]}")
    elif opc == "4":
        indice = 0
        print("\n-----------Lista de productos-----------")
        print("\tProducto \tCantidad \tPrecio")
        while indice < len(producto):
            print(f"\t{producto[indice]} \t{cantidad[indice]} \t{precio[indice]}")
            indice += 1
    else:
        break