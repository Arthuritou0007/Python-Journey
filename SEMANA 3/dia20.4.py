personaje = {
    "vida": 100,
    "oro": 200,
    "mochila": ["Daga oxidada"]
}

tienda = [
    {"nombre": "Espada Berserker", "precio": 1000},
    {"nombre": "Pócima", "precio": 200},
    {"nombre": "Pan", "precio": 100},
    {"nombre": "Mapa Misterioso", "precio": 200}
]

while True:
    mapa = False
    for i in personaje["mochila"]:
        if i == "Mapa Misterioso":
            mapa = True
    print(f"--======== ¡Bienvenido a LK Dungeon Quest! ========--")
    print(f"Tu inventario: {personaje['mochila']}")
    print(f"¿Qué quieres hacer?")
    print(f"1. Explorar la zona")
    print(f"2. Quedarse en el lugar")
    if mapa == True:
        print("¡Tienes un mapa misterioso en tu inventario!")
        print(f"3. Opción bonus: Misión especial.")
    elección = int(input("Ingrese su respuesta: "))
    if elección == 1:
            print(f"Has caminado un largo sendero y encontraste una tienda.")
            print(f"¿Quieres ver qué hay en ella?")
            print(f"1. Sí")
            print(f"2. No")
            elección = int(input("Ingrese su respuesta: "))
            if elección == 1:
               print("Has entrado a la tienda.")
               print("Un hombre encapuchado se acerca a ti y por arte de magia hace aparecer 3 objetos encima del mostrador.")
               print(f"1. {tienda[0]["nombre"]} ${tienda[0]["precio"]}")
               print(f"2. {tienda[1]["nombre"]} ${tienda[1]["precio"]}")
               print(f"3. {tienda[2]["nombre"]} ${tienda[2]["precio"]}")
               print(f"4. {tienda[3]["nombre"]} ${tienda[3]["precio"]}")
               print("5. Salir de la tienda")
               print(f"Oro: {personaje['oro']}")
               elección = int(input("Ingresa qué objeto quieres comprar: "))
               if elección == 1 and personaje["oro"] >= tienda[0]["precio"]:
                   personaje["oro"] = personaje["oro"] - tienda[0]["precio"]
                   print(f"¡Has comprado {tienda[0]["nombre"]}")
                   personaje["mochila"].append(tienda[0]["nombre"])
                   continue
               elif elección == 2 and personaje["oro"] >= tienda[1]["precio"]:
                   personaje["oro"] = personaje["oro"] - tienda[1]["precio"]
                   print(f"¡Has comprado {tienda[1]["nombre"]}")
                   personaje["mochila"].append(tienda[1]["nombre"])
                   continue
               elif elección == 3 and personaje["oro"] >= tienda[2]["precio"]:
                   personaje["oro"] = personaje["oro"] - tienda[2]["precio"]
                   print(f"¡Has comprado {tienda[2]["nombre"]}")
                   personaje["mochila"].append(tienda[2]["nombre"])
                   continue
               elif elección == 4 and personaje["oro"] >= tienda[3]["precio"]:
                   personaje["oro"] = personaje["oro"] - tienda[3]["precio"]
                   print(f"¡Has comprado {tienda[3]["nombre"]}")
                   personaje["mochila"].append(tienda[3]["nombre"])
                   continue
               elif elección == 5:
                   print("Has vuelto por donde viniste.")
                   continue
               else:
                   print("¡No tienes dinero suficiente para comprar ese objeto!")
            elif elección == 2:
                print("No te has movido ni un pelo... Otra vez.")
                continue
    elif elección == 2:
        print("No has movido ni un pelo...")
        continue
    elif elección == 3 and mapa == True:
        print("¡Has completado la misión especial y has conseguido $1000 chelines! ¡Felicidades!")
        print(f"Vida restante: {personaje['vida']}")
        personaje["oro"] = personaje["oro"] + 1000
        print(f"Balance actual: {personaje['oro']}")
        personaje["mochila"].remove("Mapa Misterioso")
        mapa = False
    elif elección == 3 and mapa == False:
        print("¡Tramposo! Elige 1 o 2.")