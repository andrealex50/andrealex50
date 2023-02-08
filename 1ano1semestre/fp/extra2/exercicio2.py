d={}
def readFile(d):
    with open('Jornadas.csv', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().split(',')
            if line[0] not in d.keys():
                d[line[0]] = []
            d[line[0]].append(line[1:])
        return d
        
def jogosdajornada(jornada, d, nomedajornada):
    jornadaselecionada = d[jornada]
    n=1
    for jogo in jornadaselecionada:
        n+=1
        valorespossiveisaposta = '12x'
        aposta = input((str(jornada) + ' ' + str(jogo[0]) + ' vs ' + str(jogo[1]) + ': '))
        while True:
            if aposta not in valorespossiveisaposta:
                aposta = input((str(jornada) + ' ' + str(jogo[0]) + ' vs ' + str(jogo[1]) + ': '))
            else:
                break
        with open(nomedajornada, 'a', encoding='utf-8') as file:
            file.write(str(n) + ', ' + aposta + '\n')
        
def resultados(nomedajornada):
    d = {}
    print(nomedajornada)
    with open(nomedajornada, 'r', encoding='utf-8') as apostas:
        for line in apostas:
            line = line.strip().split(',')
            if line[0] not in d.keys():
                d[line[0]] = ''
            d[line[0]] += line[1]
    with open('Jogos.csv', 'r', encoding='utf-8') as resultados:
        jogoslista=[]
        for line in resultados:
            line = line.strip().split(',')
            jogoslista.append(line)
        jogosdestajornada = jogoslista[((int(nomedajornada[-5])-1)*9):(int(nomedajornada[-5])*9)]
        for t in jogosdestajornada:
            indeque = jogosdestajornada.index(t)
            print('{:<5} {:>20} {:>1} - {:>1} {:>2} :{:<10}'.format((indeque+1),t[1],t[3],t[4],t[2],d[str(indeque+2)]))
def main():
    while True:
        jornada = input('Jornada? ')
        if not jornada.isdigit() and (int(jornada) > 13 or int(jornada) < 1) :
            print('Jornada inválida!')
            jornada = input('Jornada? ')
        else:
            readFile(d)
            nomedajornada = 'jornada'+str(jornada)+'.csv'
            jogosdajornada(jornada, d, nomedajornada)
            resultados(nomedajornada)

            


if __name__=='__main__':
    main()