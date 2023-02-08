n_termos = int(input('número de termos? '))
primeiro = int(input('primeiro: '))
soma = 0
termo = 0
nextterm = 0
while termo < n_termos:
    nextterm = primeiro + nextterm*10
    soma += nextterm
    termo += 1
print(soma)

