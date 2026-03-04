'''Una tienda ofrece una promoción, por la compra de 3 articulos, el costo
del elemento de menor valor tiene un descuento del 50%'''

articulo_1 = int(input("ingrese el valor del primer producto"))
articulo_2 = int(input("ingrese el valor del segundo producto"))
articulo_3 = int(input("ingrese el valor del tercer producto"))

if articulo_1 <= articulo_2 and articulo_1 <= articulo_3:
    menor = articulo_1

elif articulo_2 <= articulo_1 and articulo_2 <= articulo_3:
    menor = articulo_2

else:
    menor = articulo_3

descuento = menor * 0.50

total = articulo_1 + articulo_2 + articulo_3 - menor + descuento

print("El valor total de la compra es: ${total}")



   

