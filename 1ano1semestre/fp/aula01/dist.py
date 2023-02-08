dist = (((2*4)*9 + (2*4)*6 + (2*4)*3))*365/1000
dano = dist/1000
print(dano)
horas = dist/3600
print(horas)

andares = float(input('Andares? '))
moradores = float(input('Moradores? '))
a1 = 3*(4*moradores)
an = (andares*3)*(moradores*4)
altura = ((a1+an)*moradores)/2
alturaporano = (altura * 365)/1000
print('O elevador percorre {} por ano'.format(alturaporano))

alturatempo = (alturaporano * 1000)/3600
print('O elevador está em funcionamento {} horas'.format(alturatempo))






