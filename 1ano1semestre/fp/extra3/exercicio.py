fname="Soccer_Football Clubs Ranking.csv"
lst=[]
def readFile(fname, lst):
    with open(fname, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            line = line.strip().split(',')
            line = tuple(line)
            lst.append(line)
        return lst
readFile(fname, lst)


def countrysearch(country):
    for line in lst:
        if line[2] == country:
            print(line[1], line[0], line[3])



output = 'output.txt'
def write_clubs_by_country(lst, country, output):
    with open(output, 'w', encoding='utf-8') as file:
        for club in lst:
            if club[2] == country:
                u = club[1] + club[0] + club[3] + '\n'
                file.write(u)



def dicionario_chave_paissede(lst):
    d={}
    for club in lst:
        if club[2] not in d.keys():
            d[club[2]] = []
        d[club[2]].append(club[1])
    return d




def oquesubiumais(lst):
    subiumais = 0
    pontosdoquesubiumais = 0
    for club in lst:
        if int(club[3])-int(club[5]) > pontosdoquesubiumais:
            subiumais = club
    return subiumais



def existeounao (clubname, lst):
    for club in lst:
        if club[1] == clubname:
            return club
    return 'O clube não existe'



def rankingMedio(lst):
    paises={}
    for club in lst:
        if club[2] not in paises.keys():
            paises[club[2]] = [0,0]
        paises[club[2]][0] += int(club[3])
        paises[club[2]][1] += 1
    listarankings = []
    for pais in paises:
        numeros_pais = paises[pais]
        ranking = numeros_pais[0] / numeros_pais[1]
        listarankings.append([pais, ranking])
        listarankings = sorted(listarankings, key=lambda x: x[1])
        for paisordenado in listarankings:
            print(paisordenado[0],':', '{:.2f}'.format(paisordenado[1]))

MENU = '''
--------------
Prima (1) para pesquisar por país:
Prima (2) para escrever em outro ficheiro as informações do país introduzido:
Prima (3) para mostrar todos os clubes de cada país:
Prima (4) para indicar o clube que mais subiu no ranking:
Prima (5) para verificar se o clube existe:
Prima (6) para apresentar os paises com melhor ranking médio:
Prima (0) para sair:
--------------
>>>>>
'''

def main():
    while True:
        valorintroduzido = input(MENU)
        if valorintroduzido == '1':
            country = input('País: ')
            countrysearch(country)
        if valorintroduzido == '2':
            write_clubs_by_country(lst, country, output)
            print('Valor escritos com sucesso no ficheiro de nome "output.txt"')
        if valorintroduzido == '3':
            print(dicionario_chave_paissede(lst))
        if valorintroduzido == '4':
            print(oquesubiumais(lst))
        if valorintroduzido == '5':
            clubname = input('Nome do clube: ')
            print(existeounao (clubname, lst))
        if valorintroduzido == '6':
            rankingMedio(lst)
        if valorintroduzido == '0':
            print('Programa a encerrar')
            exit()

if __name__ == '__main__':
    main()



