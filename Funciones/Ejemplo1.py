# Crear una funcion que calcule el faactorial de un número y lo retorne 

def factorial(numero):
    # si el numero es 0 el factorial es 1
    # si el numero es menor que 0 retornar -1
    # Multiplicar desde 1 hasta numero y acumular el resultado
    if numero < 0:
          return "error"
    acumulador = 1
    for factor in range(1,numero+1):
            acumulador = acumulador * factor
            #acumulador *= factor
    return acumulador
        
    
resultado = factorial(6)
print(resultado)