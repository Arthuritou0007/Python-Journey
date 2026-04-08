def detector_bisiesto(año):
    if año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 400 == 0:
        return True
    else:
        return False
    
año_dado = int(input("Ingrese el año que quiere analizar: "))

if detector_bisiesto(año_dado):
    print("Es bisiesto.")
else:
    print("No es bisiesto.")