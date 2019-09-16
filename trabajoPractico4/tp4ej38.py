numeroIngresado = int(input("Ingrese un número para obtener la conjetura de Ullman: "))
conjeturaUllman = ""
cantDeTerminos = 0

while numeroIngresado > 1:
    if numeroIngresado % 2 == 0:
        numeroIngresado = numeroIngresado / 2
        conjeturaUllman = conjeturaUllman + str(numeroIngresado) + ""
        cantDeTerminos = cantDeTerminos + 1
    else:
        numeroIngresado = numeroIngresado * 3 + 1
        conjeturaUllman = conjeturaUllman + str(numeroIngresado) + ""
        cantDeTerminos = cantDeTerminos + 1


print("La conjetura de Ullman es: ", conjeturaUllman)
print("La cantidad de elementos de la conjetura es: ", cantDeTerminos)
