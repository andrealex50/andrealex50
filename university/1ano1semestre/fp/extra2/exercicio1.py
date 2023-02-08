MENU ='''
1) Registar chamada
2) Ler ficheiro
3) Listar clientes
4) Fatura
5) Terminar
Opção? '''
lst=[]

def validPhoneNumber(phone):
    if (len(phone) > 2 and phone.isdigit()) or (len(phone) > 2 and phone[0] == '+' and phone[1:].isdigit()):
        return True
    else:
        return False


def readfileChamadas(fname, lst):
    with open(fname, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().split()
            lst.append(line)
        return lst

def lstclientes(lst):
    lista = []
    for phone in lst:
        if phone[0] not in lista:
            lista.append(phone[0])
    listaordenada = sorted(lista)
    return listaordenada


def main():
    while True:
        menu = input(MENU)
        if menu == '1':
            origem = input('Telefone origem? ')
            while True:
                if validPhoneNumber(origem):
                    break
                else:
                    origem = input('Telefone origem? ')
            destino = input('Telefone destino? ') 
            while True:
                if validPhoneNumber(destino):
                    break
                else:
                    destino = input('Telefone destino? ') 
            duracao = input('Duração (s)? ')
        if menu == '2':
            fname = input('Ficheiro? ')
            while True:
                try:
                    readfileChamadas(fname, lst)
                    break
                except FileNotFoundError:
                    print('Nome de ficheiro inválido ou não encontrado')
                    fname = input('Ficheiro? ')
                    readfileChamadas(fname, lst)
        if menu == "3":
            print(lstclientes(lst))





if __name__ == '__main__':
    main()
       
