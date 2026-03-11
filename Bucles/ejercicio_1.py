# Solicitar dos números al usuario e imprimir los valores pares que hay entre dichos números.

numero_1 = int(input("Ingrese el primer número"))
numero_2 = int(input("Ingrese el segundo número"))

# Identificar cual es el menor y mayor 
if numero_1 > numero_2:
    mayor = numero_1
    menor = numero_2

else:
    mayor = numero_2
    menor = numero_1

while menor >= mayor:
    residuo = menor % 2
    if residuo == 0:
        print(menor)
    menor += 1
    