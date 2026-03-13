edad = int(input("Ingrese su edad: "))

if edad >= 0 or edad <=125:
    if edad < 6:
        etapa = "infancia"
    elif edad < 12:
        etapa = "Niñez"
    elif edad < 20:
        etapa = "Adolecencia"
    elif edad < 25:
        etapa = "juventud"
    elif edad < 60:
        etapa = "Adultez"
    elif edad <= 125:
        etapa = "Vejez"
    print(f"Edad en el rango: {etapa}")
else:
    print("El  numero ingresado no es una edad valida")