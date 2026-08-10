import json

datos_recuperados = 0

with open("boxeador_chamorro.json", "r", encoding="utf-8") as archivo:

    datos_recuperados = json.load(archivo)

print(f'{datos_recuperados["nombre"]}\n{datos_recuperados["estadisticas"]["victorias"]}')