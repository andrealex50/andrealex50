# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.


# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json
from collections import Counter
# Abre o ficheiro e descodifica-o criando o objeto twits.
lst=[]
with open("twitter.json", encoding="utf8") as f:
    twits = json.load(f)

words = []

# percorre cada twit no arquivo
for tweet in twits:
    # separa o texto do twit em uma lista de palavras
    tweet_words = tweet["text"].split()
    # adiciona cada palavra à lista words
    for word in tweet_words:
        words.append(word)

sohash=[]
for word in words:
    if word[0] == "#":
        sohash.append(word)
print(sohash)
# imprime a lista de palavras

# cria um dicionário para armazenar a contagem de cada palavra
word_count = Counter(words)

# ordena o dicionário pelas contagens das palavras
sorted_words = sorted(word_count.items(), key=lambda x: x[1])

#imprime a lista ordenada


# Analise os resultados impressos para perceber a estrutura dos dados.
print(type(twits))       # deve indicar que é uma lista!
print(type(twits[0]))    # cada elemento da lista é um dicionário.
print(twits[0].keys())   # mostra as chaves no primeiro elemento.

# Cada elemento contém uma mensagem associada à chave "text":
print(twits[0]["text"])

# Algumas mensagens contêm hashtags:
print(twits[880]["text"])

