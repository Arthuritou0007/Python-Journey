edad = int(input("Ingrese su edad: "))

while edad < 18:
    print("Sos menor, no podés pasar.")
    edad = int(input("Ingrese su edad nuevamente: "))

print("Acceso permitido")