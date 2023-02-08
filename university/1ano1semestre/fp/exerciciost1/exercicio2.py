def createlist():
    numeroslista=[]
    while True:
        numeros = input('Introduza números, (vazio para quando acabar): ')
        if numeros == '':
            break
        numeroslista.append(int(numeros))
    return numeroslista

k = int(input('Primeiros... :'))
def somanosk(lista,k):
    klist=lista[:k]
    res = 0
    for n in klist:
        if abs(n)/100 > 1:
            res += n
    return res

def main():
    lista = createlist()
    out = somanosk(lista,k)
    return print(out)
    
main()

   
