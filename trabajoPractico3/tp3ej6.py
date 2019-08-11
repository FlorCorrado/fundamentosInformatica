numPaginas = int(input("Ingrese el número de páginas que tiene el libro: "))
costoBasico = 125 + numPaginas * 2.20


if 300 < numPaginas < 600:
    costoBasico = costoBasico + 80
    print("El costo del libro es de:", costoBasico)
elif numPaginas > 600:
    costoBasico = costoBasico + 136
    print("El costo del libro es de:", costoBasico)
else:
    print("El costo del libro es de:", costoBasico)
