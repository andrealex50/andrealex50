def formarlista():
    i = 0
    lst=[]
    while i >= 0:
        n = input('Número a acrescentar: ')
        if n=='':
            break
        v = int(n)
        lst.append(v)
        i += 1
    return lst

def termospares(lista):
    pares = []
    for l in lista:
        if l%2 == 0 and lista.index(l)%2 != 0:
            pares.append(l)
    return pares

def main():
    lista = formarlista()
    pares = termospares(lista)
    somadetermospares = sum(pares)
    print('A soma dos números pares introduzidos é', somadetermospares )

main()