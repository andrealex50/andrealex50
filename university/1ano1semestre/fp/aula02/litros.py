quantidade = float(input('Quantidade de litros?' ))
preco1 = quantidade * 1.4
preco2 = (quantidade * 1.4) * 0.90
if quantidade <= 40 :
   print('O preço a pagar é ', preco1)
else :
   print('O preço a pagar é ', preco2)