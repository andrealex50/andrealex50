# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

produtos={}
def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname,'r', encoding="utf-8") as file:
        for line in file:
            linhaprodutos = line.strip().split(';')
            codigo = linhaprodutos[0]
            descricao_produto = tuple(linhaprodutos[1:5])
            if codigo not in produtos:
                produtos[codigo] = descricao_produto
        return produtos


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    unidades = {}
    while True:
        code = input('Code? ')
        if code not in produtos.keys() and code != '':
            code = input('Code? ')
        elif code == '':
            break
        else:
            if code not in unidades.keys():
                unidades[code] = 0
            unidades[code] += 1   
            quantidade = 1
            selected_product = produtos[code]
            nome = selected_product[0]
            preco_base = float(selected_product[2])
            taxa = selected_product[3]
            taxa = float(str(taxa).strip('%'))
            preco_final = preco_base*((100+taxa)/100)
            print(nome, quantidade, ('%.2f'%preco_final))      
    return unidades 


def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    listaprodutos = list(compra.keys())
    total_bruto = 0
    total_iva = 0
    d_seccao = {}
    for produto in listaprodutos:
        quantidade = compra[produto]
        produto = produtos[produto]
        nome = produto[0] 
        seccao = produto[1] 
        taxa = produto[3]
        taxa_for_calculus = float(str(taxa).strip('%'))
        preco_base = float(produto[2])
        preco_final = preco_base*((100+taxa_for_calculus)/100)
        preco_final = quantidade * float(preco_final)
        total_bruto += (float(preco_base)*quantidade)
        total_iva += (float(preco_final)-(preco_base*quantidade))
        preco_final = ('%.2f'%preco_final)
        tudo_menos_seccao = (quantidade, nome, taxa, preco_final)
        if seccao not in d_seccao.keys():
            d_seccao[seccao] = []
        d_seccao[seccao].append(tudo_menos_seccao)
    for mercearia in d_seccao.keys():
        d_seccao[mercearia]
        print(mercearia)
        for linha in d_seccao[mercearia]:
            quantidade = linha[0]
            nome = linha[1]
            taxa = str(linha[2])
            preco_final = linha[3]
            comp = 8 - len(str(preco_final))
            space = ' '
            if len(taxa) == 3:
                print('  ',"{:<2}{:<31}{}".format(quantidade, nome, '('+taxa+')'), space*comp, preco_final)
            else:
                print('  ',"{:<2}{:<31}{}".format(quantidade, nome, '( '+taxa+')'), space*comp, preco_final)
    total_liquido = total_bruto + total_iva
    text1 = 'Total Bruto:'
    text2 = 'Total IVA:'
    text3 = 'Total Liquido:'
    print("{:>41}{:>10}".format(text1, '%.2f'%total_bruto))
    print("{:>41}{:>10}".format(text2, '%.2f'%total_iva))
    print("{:>41}{:>10}".format(text3, '%.2f'%total_liquido))        
        

def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup', 'Mercearia Salgado', 1.59, '23%')}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)   
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    num_compra=[]
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...               
            num_compra.append(compra)
        # Acrescente outras opções aqui...
        if op == "F":
            if not num_compra:
                op = input(MENU).upper()
            else:
                numero = int(input('Numero compra? '))
                compra = num_compra[(numero-1)]
                fatura(produtos, compra)
        if op == "S":
            break

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
