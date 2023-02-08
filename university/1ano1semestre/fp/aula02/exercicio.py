import math
raio = float(input('Raio da circunferência? '))
x = float(input('Valor de X? '))
y = float(input('Valor de Y? '))

d = x*x + y*y
distancia = math.sqrt(d)

if distancia > raio:
   print('O ponto está fora da circunferência')
else:
   print('O ponto está dentro da circunferência')
a = x/distancia
angulosetor = math.acos(a)
if x < 0:
   if y < 0:
      angulo = angulosetor + (math.pi)
   else:
      angulo = angulosetor + (math.pi)/2
else:
   if y < 0:
      angulo = angulosetor + (math.pi)*(3/2)
   else:
      angulo = angulosetor
 
graus = (180*angulo)/(math.pi)

print('O ângulo com o eixo Ox é igual a ', graus)


