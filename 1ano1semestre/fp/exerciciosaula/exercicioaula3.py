import random
lst = []
d={}
def readfile():
    with open('P4.csv','r',encoding='utf-8') as file:
        next(file)
        for line in file:
            line = line.strip().split(';')
            line.append(random.randint(1, 4))
            allname = line[0]
            allname = allname.split()
            iniciais = ''
            for name in allname:
                inicial = name[0]
                iniciais += inicial
            if iniciais not in d:
                d[iniciais] = tuple(line[1:])
        return d

def atualizarvalor(op):
    valor = d[op]
    valor = list(valor)
    valor.append(pas)
    valor = tuple(valor)
    return valor

readfile()        
chaveinp = 'Introduz chave: '
op = input(chaveinp).upper()
while op not in d:
    print('Introduz uma chave válida!')
    op = input(chaveinp).upper()
else:
    print(d[op])
    pas = input('Acrescente: ')
    print(atualizarvalor(op))

        