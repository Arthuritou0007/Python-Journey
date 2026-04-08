def buscar_arma(bolso):
    arma_legendaria = 0
    for i in bolso:
        if i == "Dragon Slayer":
            arma_legendaria = True
            break
        else:
            arma_legendaria = False
            continue
    
    if arma_legendaria == True:
        return "¡Arma legendaria equipada!"
    else:
        return "Aquí solo hay chatarra."
    
        
inventario = ["poción", "daga", "Dragon Slayer", "mapa"]
        
print(buscar_arma(inventario))