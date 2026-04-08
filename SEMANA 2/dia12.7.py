while True:
    temperatura = int(input("Ingrese la temperatura actual del reactor: "))
    if temperatura >= 100:
        print("¡PELIGRO! Reactor inestable. Abortando.")
        break
    else:
        print("Temperatura estable.")