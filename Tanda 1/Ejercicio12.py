n = int(input("Introduce un número para su máximo en dominó "))

for i in range(n + 1):
    for j in range(i, n + 1):
        print(i, j)