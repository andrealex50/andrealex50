def inputFloatList():
    i=0
    lst = []
    while True:
        n = input('Número? ')
        if n == '':
            break
        i+=1
        v = int(n)
        lst.append(v)
    return lst

def CountLower(lst, v):
    c = 0
    for l in lst:
        if l < v:
            c+=1
        return c

def Minmax(lista):
    min = lista[0]
    max = lista[0]
    for j in lista:
        if j > max:
            max = j
        elif j < min:
            min = j
    return min, max

def main():
    lista = inputFloatList()
    minmax = Minmax(lista)
    minmax_media = (minmax[0] + minmax[1])/2
    contagem = CountLower(lista, minmax_media)
    print("Lista:", lista)
    print("Minimo: {}, Maximo: {}, Media: {}".format(minmax[0],minmax[1],minmax_media))
    print("Numeros abaixo da media:", contagem)

main()


        
        

        
