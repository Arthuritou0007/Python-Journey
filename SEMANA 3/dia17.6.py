def calcular_propina(total, propina):
    cuenta = total / 100
    return cuenta * propina

cuenta = 1000
propina_dada = int(input(f"Su cuenta es de ${cuenta}. Ingrese el porcentaje de propina que quiere dejar: "))

total_propina = calcular_propina(cuenta, propina_dada)

print(f"La propina que dejó es de ${int(total_propina)}, la tarifa total es de ${int(total_propina + cuenta)}")