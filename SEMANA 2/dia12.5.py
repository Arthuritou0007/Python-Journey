temperatura = int(input("Ingrese la temperatura actual: "))

while temperatura <= 99:
    print("TODO OK.")
    temperatura = int(input("Ingrese la temperatura actual: "))
    if temperatura >= 100:
        print("¡PELIGRO! Reactor sobrecalentado")
        break
else:
    print("¡PELIGRO! Reactor sobrecalentado")