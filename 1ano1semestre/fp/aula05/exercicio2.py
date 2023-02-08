lst = []
def inputFloatList():
    while True:
        number = input('Introduz número: ')
        if number != '':
            lst.append(float(number))
        else:
            break
    return lst
inputFloatList()


v = float(input('Valor v: '))
def countLower(lst, v):
    contagem = 0
    for number in lst:
        if number < v:
            contagem += 1
    return contagem


def minmax(lst):
    minimo = lst[0]
    maximo = lst[0]
    for number in lst:
        if number <= minimo:
            minimo = number
        elif number >= maximo:
            maximo = number
    valormedio = maximo+minimo / 2
    return valormedio

def valormedio(lst):
    cont = 0
    for number in lst:
        if number<minmax(lst):
            cont += 1
    return cont

print(valormedio(lst))
