# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")
x = float(input('x? '))
y = float(input('y? '))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...
import math
from traceback import print_tb
# módulo de x e y, para calcular a distância ao centro
mod = x**2 + y**2
modulo = math.sqrt(mod)
# ang é o angulo dos primeiros dois quadrantes com o eixo Ox
# adiciono pi para o terceiro quadrante e 2pi para o segundo
ang = math.acos(x / modulo)
if y > 0:
    angulo = ang
else:
    if x < 0 :
        angulo = ang + math.pi
    else:
        angulo = ang + 2*math.pi


if (39/10)*math.pi <= angulo <= (1/20)*math.pi :
    pontuacao = 6
elif (1/20)*math.pi < angulo <= (3/20)*math.pi :
    pontuacao = 13
elif (3/20)*math.pi < angulo <= (1/4)*math.pi :
    pontuacao = 4
elif (1/4)*math.pi < angulo <= (7/20)*math.pi :
    pontuacao = 18
elif (7/20)*math.pi < angulo <= (9/20)*math.pi :
    pontuacao = 1
elif (9/20)*math.pi < angulo <= (11/20)*math.pi :
    pontuacao = 20
elif (11/20)*math.pi < angulo <= (13/20)*math.pi :
    pontuacao = 5
elif (13/20)*math.pi < angulo <= (3/4)*math.pi :
    pontuacao = 12
elif (3/4)*math.pi < angulo <= (17/20)*math.pi :
    pontuacao = 9
elif (17/20)*math.pi < angulo <= (19/20)*math.pi :
    pontuacao = 14
elif (19/20)*math.pi < angulo <= (21/10)*math.pi :
    pontuacao = 11
elif (21/10)*math.pi < angulo <= (23/20)*math.pi :
    pontuacao = 8
elif (23/20)*math.pi < angulo <= (5/4)*math.pi :
    pontuacao = 16
elif (5/4)*math.pi < angulo <= (27/20)*math.pi :
    pontuacao = 7
elif (27/20)*math.pi < angulo <= (29/20)*math.pi :
    pontuacao = 19
elif (29/20)*math.pi < angulo <= (31/20)*math.pi :
    pontuacao = 3
elif (31/20)*math.pi < angulo <= (33/20)*math.pi :
    pontuacao = 17
elif (33/20)*math.pi < angulo <= (7/4)*math.pi :
    pontuacao = 2
elif (7/4)*math.pi < angulo <= (37/20)*math.pi :
    pontuacao = 15
elif (37/20)*math.pi < angulo <= (39/20)*math.pi :
    pontuacao = 10
elif (39/20)*math.pi < angulo <= (2)*math.pi :
    pontuacao = 6


if modulo <= 6.35 :
   score = 50
elif 6.35 < modulo <= 16 :
   score = 25
elif 16 < modulo <= 99 :
   score = pontuacao * 1
elif 99 < modulo <= 107 :
   score = pontuacao * 3
elif 107 < modulo <= 162 :
   score = pontuacao * 1
elif 162 < modulo <= 170 :
   score = pontuacao * 2

print(score)



