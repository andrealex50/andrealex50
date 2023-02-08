texto = input('Introduza o texto: ')
def read():
    lst=[]
    for n in texto:
        lst.append(n)
    return lst

def consonants(lista):
    consoantes = 0
    for u in lista:
        if u not in ['a','e','i','o','u','A','E','I','O','U']:
            consoantes += 1
    return consoantes

def main():
    lista = read()
    out = consonants(lista)
    return print(out)

main()

#não acabado