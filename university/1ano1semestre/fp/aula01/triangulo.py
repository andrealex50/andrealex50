a = float(input('Comprimento do cateto A? '))
b = float(input('Comprimento do cateto B? '))
import math
c1 = a*a + b*b
c = math.sqrt(c1)
angulo = math.acos(a/c)
print('O valor de C é {}, e o valor do ângulo CÂB é {}'.format(c, angulo))


