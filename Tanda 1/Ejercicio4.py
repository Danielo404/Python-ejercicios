pregunta = True

while pregunta:
    n = input("Introduce el número de amigos que tienes ")
    try:
        n = int(n)
        pregunta = False
    except ValueError:
        print("Lo que has introducido no es un número")

for i in range(n):
    amiwi = input("Como se llama tu amiwi?")
    print("Que pasa ", amiwi)