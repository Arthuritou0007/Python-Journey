nota_1 = int(input("Ingrese la primera nota aquí:"))
nota_2 = int(input("Ingrese la segunda nota aquí:"))
nota_3 = int(input("Ingrese la tercera nota aquí:"))

promedio = (nota_1 + nota_2 + nota_3) / 3

if promedio >= 6:
    print("¡Aprobaste la materia! Su promedio es de", promedio)
else:
    print("No aprobaste la materia. Su nota es de", promedio)