andares = int(input("Andares? ")) # numero além do R/C
moradores = int(input("Moradores por andar? "))
altura = 3 # altura de um andar (m)
vel = 1 # m/s
# distancia percorrida num ano (m)
dist = 365 * altura * 4 * moradores * (andares + 1) * andares / 2
segundos = dist / vel
horas = segundos / 3600
print(dist/1000, "km")
print(horas, "h")