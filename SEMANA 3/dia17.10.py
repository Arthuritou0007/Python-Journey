def es_primo(numero):
    divisores = 0
    
    # CORRECCIÓN 1: Empezamos en 1 y vamos hasta el número INCLUIDO (+1)
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores = divisores + 1
            
    # CORRECCIÓN 2: Si tiene 2 divisores (el 1 y el mismo)... ¡ES PRIMO!
    if divisores == 2:
        return True  # Antes tenías False
    else:
        return False # Antes tenías True

# --- Probamos ---
numero_dado = int(input("Ingrese el número: "))

if es_primo(numero_dado):
    print("Es primo")
else:
    print("No es primo")