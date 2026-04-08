def celcius_a_fahrenheit(grados):
    fahrenheit = (grados * 9/5) + 32
    return fahrenheit

grados_dados = int(input("Ingrese los grados que quiera convertir: "))

print(f"{grados_dados}° es igual a {celcius_a_fahrenheit(grados_dados)}°F")