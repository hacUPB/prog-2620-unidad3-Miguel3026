altura_visitante = float(input("Ingrese la altura del visitante en cm:"))
estatura_minima = 150 
cumple_requisito = altura_visitante >= estatura_minima
no_cumple = altura_visitante < estatura_minima
print("puede subir  ", cumple_requisito)
print("no puede subir  ", no_cumple)