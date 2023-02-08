# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

produtos={}
def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname,'r', encoding="utf-8") as file:    #abrir o ficheiro
        next(file)   #ignorar primeira linha do ficheiro
        for line in file:   
            linhaprodutos = line.strip().split(';')
            codigo = linhaprodutos[0]
            linhaprodutos[4] = float((linhaprodutos[4]).strip('%'))/100    #passar 23% para 0.23 por exemplo
            linhaprodutos[3] = float(linhaprodutos[3])
            descricao_produto = tuple(linhaprodutos[1:5])   #criar tuplo com tudo menos o código
            if codigo not in produtos:    
                produtos[codigo] = descricao_produto    #criar dicionário com o codigo como chave
        return produtos


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    unidades = {}     
    while True:
        codeimp = input('Code? ')
        if codeimp == '':   #input vazio para fechar a função e prosseguir
            break
        else:
            lst = codeimp.split()
            code = lst[0]   #código é o primeiro elemento da lista
            while code not in produtos.keys():  #verificar se o código está no dicionário produtos, se não pedir de novo um input
                codeimp = input('Code? ')
                if codeimp == '':
                    break
                else:
                    lst = codeimp.split()
                    code = lst[0]
            else:
                if code == codeimp:   #se código for o único presente na lista
                    if code not in unidades.keys():   #criar dicionário com quantidades
                        unidades[code] = 0
                    unidades[code] += 1   
                    quantidade = 1   #quantidade a dar print igual a 1 por predefinição
                else:
                    quantidade = int(lst[1])   #se a lista tiver mais de um elemento, o segundo é a quantidade
                    while quantidade <= 0 or code not in produtos.keys():
                        codeimp = input('Code? ')
                        if codeimp == '':
                            break
                        else:
                            lst = codeimp.split()
                            code = lst[0]
                            if len(lst)==1:   #se o comprimento da nova lista for 1
                                quantidade = 1
                            else:   #se o comprimento da nova lista for mais que 1  
                                quantidade = int(lst[1])   #o segundo elemento vai ser a quantidade
                    if code not in unidades.keys():  #criar/atualizar dicionário com os novos valores de unidades
                        unidades[code] = 0
                    unidades[code] += quantidade   
                selected_product = produtos[code]
                nome = selected_product[0]
                preco_base = float(selected_product[2])
                taxa = selected_product[3]
                preco_final = preco_base*((1+taxa))*quantidade
                print(nome, quantidade, ('%.2f'%preco_final))                     
    return unidades


def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    listaprodutos = list(compra.keys())   #transformar a compra em uma lista
    total_bruto = 0
    total_iva = 0
    d_seccao = {}
    for produto in listaprodutos:
        quantidade = int(compra[produto])
        produto = produtos[produto]
        nome = produto[0] 
        seccao = produto[1] 
        taxa = produto[3]
        preco_base = float(produto[2])
        preco_final = preco_base*((1+float(taxa)))
        preco_final = quantidade * float(preco_final)
        total_bruto += (float(preco_base)*quantidade)
        total_iva += (float(preco_final)-(preco_base*quantidade))
        preco_final = ('%.2f'%preco_final)
        tudo_menos_seccao = (quantidade, nome, taxa, preco_final)
        if seccao not in d_seccao.keys():   #criar dicionário com tudo igual menos o nome da seccão, sendo esta a chave
            d_seccao[seccao] = []
        d_seccao[seccao].append(tudo_menos_seccao)
    for mercearia in d_seccao.keys():   #dar print da chave do dicionário, ou seja a secção
        d_seccao[mercearia]
        print(mercearia)
        for linha in d_seccao[mercearia]:   #percorrer o dicionário das secções
            quantidade = linha[0]
            nome = linha[1]
            taxa = str(int(linha[2]*100))
            preco_final = linha[3]
            comp = 8 - len(str(preco_final))
            space = ' '
            if len(taxa) == 2:  #como a taxa não excede os 99% podemos dividir em dois casos, se a taxa for 2 digitos
                if len(str(quantidade))==2:  #se a quantidade for igual a 2 digitos
                    print(' ',"{:<3}{:<31}{}".format(quantidade, nome, '('+taxa+'%)'), space*comp, preco_final)
                elif len(str(quantidade))==1:  #se a quantidade for igual a 1 digitos
                    print('  ',"{:<2}{:<31}{}".format(quantidade, nome, '('+taxa+'%)'), space*comp, preco_final)
                elif len(str(quantidade))==3:   #se a quantidade for igual a 3 digitos
                    print('',"{:<4}{:<31}{}".format(quantidade, nome, '('+taxa+'%)'), space*comp, preco_final)
            else:  #se a taxa for 1 digitos
                if len(str(quantidade))==2:   #se a quantidade for igual a 2 digitos
                    print(' ',"{:<3}{:<31}{}".format(quantidade, nome, '( '+taxa+'%)'), space*comp, preco_final)
                elif len(str(quantidade))==1:   #se a quantidade for igual a 1 digitos
                    print('  ',"{:<2}{:<31}{}".format(quantidade, nome, '( '+taxa+'%)'), space*comp, preco_final)
                elif len(str(quantidade))==3:   #se a quantidade for igual a 3 digitos
                    print('',"{:<4}{:<31}{}".format(quantidade, nome, '( '+taxa+'%)'), space*comp, preco_final)
    total_liquido = total_bruto + total_iva
    text1 = 'Total Bruto:'
    text2 = 'Total IVA:'
    text3 = 'Total Liquido:'
    print("{:>41}{:>10}".format(text1, '%.2f'%total_bruto))
    print("{:>41}{:>10}".format(text2, '%.2f'%total_iva))
    print("{:>41}{:>10}".format(text3, '%.2f'%total_liquido))        
        

def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)   
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    num_compra=[]   #registra as compras numa lista
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...               
            num_compra.append(compra)   #adiciona a compra à lista
        # Acrescente outras opções aqui...
        def numberisvalid(numero, num_compra):   #função que determina se o número da fatura é válido
            if str(numero).isdigit():
                if int(numero) > len(num_compra) or int(numero) <= 0:
                    return False
                else:
                    return True
            else:
                return False
        if op == "F":
            numero = input('Numero compra? ')
            if numberisvalid(numero, num_compra) == True:
                compra = num_compra[(int(numero)-1)]   #determina o indice do número na lista num_compra e atualiza a compra com apenas essa compra
                fatura(produtos, compra)
            else:
                while numberisvalid(numero, num_compra) == False:
                    numero = input('Numero compra? ')
                    if numberisvalid(numero, num_compra) == True:
                        numero = int(numero)
                        compra = num_compra[(int(numero)-1)]
                        fatura(produtos, compra)
        if op == "S":
            break

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])