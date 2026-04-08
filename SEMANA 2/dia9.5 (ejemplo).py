edad = int(input("Ingrese su edad:"))
tiene_permiso = True # Supongamos que sí tiene permiso

if edad >= 13 and (tiene_permiso == True or edad >= 18):
    print("Puedes jugar")
else:
    print("No puedes jugar")

# Puedes jugar si tienes al menos 13 años Y (tienes permiso de tus padres O eres mayor de 18).