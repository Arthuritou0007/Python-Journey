import json

def guardar_datos(datos):
    with open(f"POO EJERCICIO 1/DATABASE/{datos['nombre']}.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)