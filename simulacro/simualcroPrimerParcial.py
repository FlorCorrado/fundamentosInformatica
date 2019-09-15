mayorValorGastado = 0
diaDeMayorGasto = 0
porcentajeRepresentativoTotalMes = 0
importeTotal = 0
menorGasto = 0

dia = int(input("Ingrese el dia del mes, si desea salir escriba -1: "))
while dia != -1:
    if 1 <= dia <= 31:
        valorGastado = int(input("Ingrese el valor gastado ese dia: "))
        importeTotal += valorGastado

        if valorGastado > mayorValorGastado:
            mayorValorGastado = valorGastado
            diaDeMayorGasto = dia

        if valorGastado < mayorValorGastado:
            menorGasto = valorGastado

    dia = int(input("Ingrese el dia del mes, si desea salir escriba -1: "))


print("El dia de mayor gasto fue: ", diaDeMayorGasto)
print("El mayor gasto fue de: ", mayorValorGastado)
print("El menor valor gastado fue: ", menorGasto)

porcentajeRepresentativoTotalMes = mayorValorGastado * 100 / importeTotal

print("El porcentaje del mayor gasto comparado con el total gastado fue de:",
      float(porcentajeRepresentativoTotalMes), "%")

