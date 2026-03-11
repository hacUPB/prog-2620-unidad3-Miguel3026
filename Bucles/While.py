# Imprimir los números del 5 al 50, pero de 5 en 5
#numero = 5
#while numero <= 50:
#    print(numero)
#    numero += 5 #numero = numero + 5

# Desde 100 hasta 50, pero unicamente los impares 

numero = 100
while numero >= 50:
    residuo = numero % 2
    if residuo == 1:
        print(numero)
    numero -= 1
    
