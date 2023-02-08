texto = input('Texto> ')
def readLst(texto):
    i=0
    lst=[]
    for n in texto:
        lst.append(n)
    return lst

def vogaischeck(lista):
    i=0
    vogais=[]
    for u in lista:
        if u.isalpha() and u.isupper() and lista.index(u)%2 == 0 and u in ['A', 'E', 'I', 'O', 'U']:
            vogais.append((lista.index(u)))
    return vogais

def main():
    lista = readLst(texto)
    vogaisupper = vogaischeck(lista)
    return print(vogaisupper)

main()