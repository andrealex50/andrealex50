# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
with open('drawing.txt','r',encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line == 'UP':
            t.up()
            while line.isdigit():
                coor = line.split()
                t.goto(coor)
        elif line == 'DOWN':
            t.down()
            while line.isdigit():
                coor = line.split()
                t.goto(coor)
        else:
            continue


# wait
turtle.Screen().exitonclick()

