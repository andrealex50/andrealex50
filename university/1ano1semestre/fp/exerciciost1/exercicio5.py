def criarlista():
    lst = []
    while True:
        numeros = input('Introduza número a adicionar: ')
        if numeros == '':
            break
        lst.append(int(numeros))
    return lst

def cresordes(lista):
    i=0
    while i < len(lista):
        u=i+1
        if lista[i]>lista[u]:
            return 'Decreasing'
        elif lista[i]<lista[u]:
            return 'Increasing'
        else:
            return 'Not a monotonic sequence'

def main():
    lista = criarlista()
    resul = cresordes(lista)
    return print(resul)

main()

