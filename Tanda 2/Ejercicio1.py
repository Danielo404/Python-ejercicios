def segundos (h, m, s):
    total = (h * 3600) + (m * 60) + s
    return total

def hora (s):
    horas = s // 3600
    s = s % 3600
    minutos = s // 60
    segundos = s % 60

    return (horas, minutos, segundos)

print(hora(5000))

print(segundos(2, 56, 20))