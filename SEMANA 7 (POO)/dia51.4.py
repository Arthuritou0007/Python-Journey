import json

datos_recuperados = 0

with open("boxeador_chamorro.json", "r", encoding="utf-8") as archivo:

    datos_recuperados = json.load(archivo)

print(datos_recuperados["historial_peleas"][0]["rival"])