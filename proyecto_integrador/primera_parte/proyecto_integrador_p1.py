#crear un menu interactivo utilizando bucles y condicionales
#implementar la funcionalidad para agregar productos a una lista
#mostrar los productos ingresados

#agregar productos al inventario y mostrar los productos registrados

#DEFINO VARIABLES
productos = []
prod_cantidad = 0
prod_precio = 0.0
opciones = [1,2,3,4,5]
buscar = ""
indice = 0

print("*** Proyecto Integrador 1ra Parte ***")

while True:
    #MENU
    print("-------- MENU --------")
    print("1-Agregar un producto")
    print("2-Buscar un producto")
    print("3-Modificar un producto")
    print("4-Ver producto")
    print("5-Salir del sistema\n")

    #SELECCION DE OPCION
    opcion = input("Seleccione una opcion 1-5: ")
    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("Opcion invalida!\n")
        continue

    if opcion == opciones[0]: #OPCION 1 - AGREGAR PRODUCTO
        prod_nombre = input("Ingrese el nombre del producto: ")
        prod_cantidad = input("Ingrese la cantidad del producto: ")
        prod_precio = input("Ingrese el precio del producto: ")
        producto = [prod_nombre, prod_cantidad, prod_precio] #DEFINO UNA LISTA DEL PRODUCTO A INGRESAR
        productos.append(producto)

        print(" ") #SALTO DE LINEA

    elif opcion == opciones[1]: #OPCION 2 - BUSCAR UN PRODUCTO
        indice = 0
        buscar = input("Nombre del producto a buscar ==> ")
        while indice < len(productos): #LEN PRODUCTOS
            if productos[indice][0].lower() == buscar.lower(): 
                print(f"{'NOMBRE':<10} {'CANTIDAD':<10} {'PRECIO':<10}")
                print(f"{productos[indice][0]:<10} {productos[indice][1]:<10} ${productos[indice][2]:<10}")
                break #SALGO DE WHILE DE OPCIONES
            indice += 1
        print(" ") #SALTO DE LINEA    

    elif opcion == opciones[2]:  # OPCION 3 - MODIFICAR UN PRODUCTO
        buscar = input("Ingrese el nombre del producto a modificar: ")
        indice = 0
        encontrado = False  #Verificar si se encuentra el producto
        
        while indice < len(productos):
            if productos[indice][0].lower() == buscar.lower():
                encontrado = True
                print(f"{'NOMBRE':<10} {'CANTIDAD':<10} {'PRECIO':<10}")
                print(f"{productos[indice][0]:<10} {productos[indice][1]:<10} ${productos[indice][2]:<10}")
                
                while True:  # MODIFICAR
                    # MODIFICAR NOMBRE
                    aux = input(f"El nombre actual es: {productos[indice][0]}, desea cambiarlo(si/no)?: ")
                    if aux.lower() == "si":
                        prod_nombre = input("Ingrese el nuevo nombre del producto: ")
                    elif aux.lower() == "no":
                        prod_nombre = productos[indice][0]
                    else:
                        print("Opción incorrecta.")
                        continue
                    
                    # MODIFICAR CANTIDAD
                    aux = input(f"La cantidad actual es: {productos[indice][1]}, desea cambiarlo(si/no)?: ")
                    if aux.lower() == "si":
                        prod_cantidad = input("Ingrese la nueva cantidad del producto: ")
                    elif aux.lower() == "no":
                        prod_cantidad = productos[indice][1]
                    else:
                        print("Opción incorrecta.")
                        continue
                    
                    # MODIFICAR PRECIO
                    aux = input(f"El precio actual es: ${productos[indice][2]}, desea cambiarlo(si/no)?: ")
                    if aux.lower() == "si":
                        prod_precio = input("Ingrese el nuevo precio del producto: ")
                    elif aux.lower() == "no":
                        prod_precio = productos[indice][2]
                    else:
                        print("Opción incorrecta.")
                        continue

                    # Actualizar el producto
                    productos[indice] = [prod_nombre, prod_cantidad, prod_precio]
                    print("Producto actualizado con éxito.")
                    break  # Sale del while interno después de la modificación
                
                print(" ")
                break  # Sale del while principal después de encontrar y modificar el producto
            
            indice += 1
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == opciones[3]: #OPCION 4 - VER PRODUCTOS
        indice = 0
        if len(productos) == 0:
            print("No hay productos almacenados!")
        else:
            print("\n*** LISTA DE PRODUCTOS ***")
            print(f"{'NOMBRE':<10} {'CANTIDAD':<10} {'PRECIO':<10}")
            while indice < len(productos):
                print(f"{productos[indice][0]:<10} {productos[indice][1]:<10} ${productos[indice][2]:<10}")
                indice += 1
        print(" ") #SALTO DE LINEA
        
    elif opcion == opciones[4]: #OPCION 5 - SALIR
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion incorrecta!")
        print(" ") #SALTO DE LINEA
        continue