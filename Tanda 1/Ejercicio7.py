def conversion(grados):
    return round((grados - 32) * 5 / 9)


print("Grados Fahrenheit     Grados Celsius")
print("=================     ==============")
for grados in range(0, 120, 10):
    print("      ", grados, "               ", conversion(grados))