menu = {"Cerveza": 50, "Guiso": 120, "Pan": 15}

personaje = {
    "mochila": ["Espada", "Trapo", "Medicina"],
    "monedero": 200,
    "armadura": ["Casco de cuero", "Pechera de cuero"],
}


print("¡Bienvenido a la caverna!")
print("¿Qué deseas comprar?")
print(f"[1] Cerveza ${menu['Cerveza']}")
print(f"[2] Guiso   ${menu['Guiso']}")
print(f"[3] Pan     ${menu['Pan']}")
print(f"Tu capital: ${personaje['monedero']}")
eleccion = int(input("Ingrese aquí la opción que desea comprar (1, 2 o 3): "))

if eleccion == 1:
    personaje["monedero"] = personaje["monedero"] - menu["Cerveza"]
    personaje["mochila"].append("Cerveza")
    print(f"¡Has comprado una Cerveza y se ha agregado a tu inventario!")
    print(f"Tu capital ahora es de {personaje['monedero']}")
elif eleccion == 2:
    personaje["monedero"] = personaje["monedero"] - menu["Guiso"]
    personaje["mochila"].append("Guiso")
    print(f"¡Has comprado un Guiso y se ha agregado a tu inventario!")
    print(f"Tu capital ahora es de {personaje['monedero']}")
elif eleccion == 3:
    personaje["monedero"] = personaje["monedero"] - menu["Pan"]
    personaje["mochila"].append("Pan")
    print(f"¡Has comprado un Pan y se ha agregado a tu inventario!")
    print(f"Tu capital ahora es de {personaje['monedero']}")