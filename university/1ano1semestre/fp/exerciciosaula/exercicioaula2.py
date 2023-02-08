def lerlista():
    frase = input('Introduz a frase: ')
    listalida = []
    for l in frase:
        i = frase.index(l)
        if l ==' ':
            listalida.append(frase[:i])
    return listalida

def primo(lista):
    palavrasprimas=[]
    for g in lista:
        y = len(g)
        if y%2 != 0 and y%3 != 0 and y != 1:
            palavrasprimas.append(g)  
    return palavrasprimas

def main():
    lista = lerlista()
    listacomprimos = primo(lista)
    print(listacomprimos)

main()

