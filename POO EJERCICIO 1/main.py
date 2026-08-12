from models import Mascota
from backend import guardar_datos

mascota_1 = Mascota("Bobby", "Perro", "Pedro", "Vómito")

datos_para_guardar = mascota_1.to_dict()

guardar_datos(datos_para_guardar)