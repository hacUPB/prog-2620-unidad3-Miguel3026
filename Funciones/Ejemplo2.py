# Función menu: imprime un menú y retorna la opción elegida por el usuario 
def menu():
    print("1. suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Selecciona una opción:"))
    return opcion

operacion = menu()
print(f"El usuario eligio la opción {operacion}")


