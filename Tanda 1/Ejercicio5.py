pregunta = True

while pregunta:
    try:
        cantidad = float(input("Introduce la cantidad de € "))
        interes = float(input("Introduce el interés % "))
        nAnnos = float(input("Introduce el número de años "))
        pregunta = False

    except ValueError:
        print("Error en los datos \n")

def resultado (c, i, nA):
    total = round(c * (1 + i/100) ** nA)
    return total

print("Total a pagar ", resultado(cantidad, interes, nAnnos), " €")


