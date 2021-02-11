n1 = int(input("Introduce el primer número "))
n2 = int(input("Introduce el segundo número "))

n1 += n1 % 2

for i in range (n1, n2 + 1, 2):
    print(i)