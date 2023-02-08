# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, 'r', encoding="utf-8") as file:
        file.readline()
        for line in file:
            line=line.strip().split('\t')
            line[0] = int(line[0])
            line[2] = int(line[2])
            line[5] = float(line[5])
            line[6] = float(line[6])
            line[7] = float(line[7])
            line = tuple(line)
            lst.append(line)
        return lst


    
# b) Crie a função notaFinal aqui...
def notaFinal (aluno):
    notafinal = (aluno[5]+aluno[6]+aluno[7]) / 3
    return "{:.1f}".format(notafinal)

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print('Numero', 'Nome'.center(50), 'Nota'.rjust(0))
    for aluno in lst:
        numero = aluno[0]
        nome = aluno[1]
        nota = notaFinal(aluno)
        print('{:>5}{}{:>6}'.format(numero,nome.center(50),nota))


# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst = sorted(lst)
    
    # mostrar a pauta
    print(printPauta(lst))


# Call main function
if __name__ == "__main__":
    main()


