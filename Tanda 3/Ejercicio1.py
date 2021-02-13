from math import sqrt


"""Dado un número entero n, indicar si es o no par."""

def esPar (n):

    if n %2 == 0:
        return  True
    else:
        return False

print(esPar(3))

"""Dado un número entero n, indicar si es o no primo."""

def primo(n):
    primo = True
    if not(n % 2):
        for i in (3, sqrt(n)+1, 2):
            if n % i == 0:
                primo = False
                break
        return primo