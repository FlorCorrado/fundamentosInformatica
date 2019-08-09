from math import trunc

segundos = int(input("Ingrese un período de tiempo en segundos: "))

dias = trunc(segundos / 86400)
restoDias = segundos % 86400

horas = trunc(restoDias / 3600)
restoHoras = restoDias % 3600

minutos = trunc(restoHoras / 60)
restoMinutos = restoHoras % 60

print("El período ingresado equivale a: ", dias, "dias",horas, "horas", minutos, "minutos", restoMinutos, "segundos")

