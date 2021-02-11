
pregunta = True

while pregunta:
    try:
        grados = float(input("¿Cuanos grados Farenheit hay? "))
        pregunta = False
    except ValueError:
        print("Hay un error en los datos\n")

def resultado (grados):
    return round((grados - 32)*5/9)

print("Hay en total de",resultado(grados),"º Celsius")