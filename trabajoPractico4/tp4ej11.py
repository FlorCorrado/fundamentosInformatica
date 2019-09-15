a = int(input("primer valor: "))
b = int(input("segundo valor: "))
cantSumas = 1
resultado = 0

while cantSumas <= b:
    resultado = resultado + a
    cantSumas = cantSumas + 1

print("resultado:", resultado)
