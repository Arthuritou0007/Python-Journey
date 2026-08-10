import json

class Pugil:
    def __init__(self, dni, nombre, gimnasio, peso, postura):
        self.dni = dni
        self.nombre = nombre
        self.gimnasio = gimnasio
        self.peso = peso
        self.postura = postura
        self.estado = "Pendiente" # El estado de aprobación
        
        # Estadísticas tipo Tapology
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0
        self.historial_peleas = [] # Acá guardaremos diccionarios con cada pelea

    # EL TRADUCTOR
    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "gimnasio": self.gimnasio,
            "peso": self.peso,
            "postura": self.postura,
            "estado": self.estado,
            "estadisticas": {
                "victorias": self.victorias,
                "derrotas": self.derrotas,
                "empates": self.empates,
                "total_peleas": self.victorias + self.derrotas + self.empates
            },
            "historial_peleas": self.historial_peleas
        }

# 1. Creamos el objeto
boxeador_1 = Pugil(12345678, "Santiago Chamorro", "Team Cobra", 66.5, "Diestro")

# 2. Le agregamos una pelea al historial
boxeador_1.historial_peleas.append({
    "fecha": "2023-10-15",
    "rival": "Juan Pérez",
    "resultado": "Victoria",
    "metodo": "KO"
})
boxeador_1.victorias += 1

# 3. Lo traducimos
datos_para_guardar = boxeador_1.to_dict()

# Imprimimos para ver la magia
print(datos_para_guardar)

# --- LA MAGIA NUEVA EMPIEZA ACÁ ---

# 2. Le decimos a Python que abra (o cree) un archivo en modo escritura ("w" = write)
with open("boxeador_chamorro.json", "w", encoding="utf-8") as archivo:
    # 3. Volcamos (dump) el diccionario adentro del archivo
    json.dump(datos_para_guardar, archivo, indent=4, ensure_ascii=False)

print("¡El archivo JSON se creó con éxito!")