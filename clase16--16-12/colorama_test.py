from colorama import init, Fore, Back, Style

#inicializar colorama
init(autoreset=True)

print(Fore.RED + "Este texto es rojo")
print(Fore.GREEN + "Este texto es verde")


print(Fore.BLUE + Back.WHITE + Style.BRIGHT + "Texto azul con fondo blanco y brillante")


#menu
print(Back.BLUE + Style.BRIGHT + "--- menu principal ---")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "1." + Style.RESET_ALL + " Registrar producto")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "2." + Style.RESET_ALL + " Consultar producto")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "3." + Style.RESET_ALL + " Actualizar producto")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "4." + Style.RESET_ALL + " Eliminar producto")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "5." + Style.RESET_ALL + " Listar productos")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "6." + Style.RESET_ALL + " Reporte de bajo stock")
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "7." + Fore.LIGHTRED_EX+ " Salir")



