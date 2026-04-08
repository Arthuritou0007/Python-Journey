kilometros = int(input("Ingrese la cantidad de km que va a viajar:"))
gasto_de_nafta = float(input("Cuánto de nafta gasta en total su auto por km:"))
precio_nafta = 100 # $1000 el lt de nafta
uso_de_nafta = kilometros * gasto_de_nafta
gasto_total = uso_de_nafta * precio_nafta

if gasto_total > 30000:
    print("Su viaje será caro.")
else:
    print("Su viaje será barato")

print("Costo total del viaje $" + str(gasto_total))