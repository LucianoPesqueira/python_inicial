opc = 0

while opc != 3:
    print("\nMenu de opciones:")
    print("1. Ver Productos")
    print("2. Agregar un Producto")
    print("3. Salir")

    opc = int(input("Selecciona una opcion: "))

    if opc == 1:
        print("Mostrando Productos...")
    elif opc == 2:
        print("Agregando un Producto...")
    elif opc == 3:
        print("Saliendo del Menu..")
        break
    else:
        print("Error, opcion incorrecta!!")

