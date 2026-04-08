def pase_vip(edad, tiene_invitacion):
    if edad >= 18 and tiene_invitacion == True:
        return True
    else:
        return False

edad_dada = int(input("Ingrese su edad: "))

print("¿Tiene invitación?")
print("1. Sí")
print("2. No")
invitacion = int(input("Ingrese aquí su respuesta: "))

if invitacion == 1:
    permiso = True
else:
    permiso = False

if pase_vip(edad_dada, permiso):
    print("Puede ingresar.")
else:
    print("No puede ingresar.")