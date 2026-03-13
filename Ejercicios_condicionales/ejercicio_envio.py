# La moneda es en Pesos Colombianos 
compra = int(input("Ingrese el valor de la compra: "))
if compra > 100000:
    print(f"El valor de la compra es de ${compra}")
else:    total = compra + 9000
print(f"El valor de la compra con envio es de ${total}")



