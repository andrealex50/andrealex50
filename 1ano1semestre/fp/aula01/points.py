# This program reads the coordinates of two points (x1,y1) and (x2,y2).

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))
import math
d1 = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
d = math.sqrt(d1)
print('A distância entre os dois pontos é {}'.format(d))
# Find and print the distance between the points!
# ...

