# Genere una constante de texto que sera la contraseña. Luego pida al usuario que ingrese la contraseña 
# Mientras la contraseña no sea correcta, debe seguir pidiendo la contraseña. Si esta correcta, deja continuar con el resto del programa.

password = "pulga1226.." 
i = input("Ingrese la contraseña")
while i == password:
    print("Ingresando al programa....")
    break
else: 
    print("contraseña incorrecta, ingresela nuevamente")