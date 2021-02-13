i = 0
leyendo = True
total = 0
print("Introduzca sus notas")
print("====================")

while leyendo:
    n = float(input("Introduzca la nota "))
    i += 1
    total = total + n
    continuar = input("¿Quieres introducir otra nota? (S/N) ")

    if (continuar in "Nn"):
        leyendo = False

print("La nota media es:", total / i)