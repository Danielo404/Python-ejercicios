n = int(input("Hasta que número quieres saber su triangular "))

resultado = 0

for i in range(1 , n + 1, 1):
    nAdicional = 1
    resultado = 0
    for j in range (1, i+1 , 1):
        resultado = resultado + nAdicional
        nAdicional += 1
    print(i, "       ", resultado)