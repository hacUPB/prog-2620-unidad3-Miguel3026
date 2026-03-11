# Función menu: imprime un menú y retorna la opción elegida por el usuario 
def menu():
    opcion = 0
    while opcion < 1 or opcion > 4: 
        print("1. suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        opcion = int(input("Selecciona una opción:"))
        if opcion < 1 or opcion > 4:
         print("la opcion elegida no es valida")
         return opcion

operacion = menu()
print(f"El usuario eligio la opción {operacion}")

if operacion == 1:
   pass
elif operacion == 2:
    pass
elif operacion == 3:
   pass
elif operacion == 4:
   pass




