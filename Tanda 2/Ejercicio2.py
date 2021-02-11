h1 = int(input("Introduce horas    1: "))
m1 = int(input("Introduce minutos  1: "))
s1 = int(input("Introduce segundos 1: "))
h2 = int(input("Introduce horas    2: "))
m2 = int(input("Introduce minutos  2: "))
s2 = int(input("Introduce segundos 2: "))

def segundos (h, m, s):
    total = (h * 3600) + (m * 60) + s
    return total

def hora (s):
    horas = s // 3600
    s = s % 3600
    minutos = s // 60
    segundos = s % 60

    return (horas, minutos, segundos)

(h, m, s) = hora(segundos(h1, m1, s1) + segundos(h2, m2, s2))

print("La suma es:", h, "horas", m, "minutos y", s, "segundos")