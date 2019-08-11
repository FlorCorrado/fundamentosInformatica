base = int(input("Ingrese la base del triámgulo: "))

altura = int(input("Ingrese la altura del triámgulo: "))

if base < 0:
    print("Verifique el número ingresado para la base del triángulo")
elif altura < 0:
    print("Verifique el número ingresado para la altura del triángulo")
else:
    print("La superficie del triángulo es: ", (base * altura) / 2)
