
# Generates all length-3 words with symbols taken from the given alphabet.
def genWords3(symbols):
    lst = []
    for x in symbols:
        for y in symbols:
            for z in symbols:
               lst.append(x+y+z)
    return lst

# Generates all length-n words with symbols taken from the given alphabet.
def genWords(symbols, n):
    l=[]
    if n==1:
        for x in symbols:
            l.append(x)
        return l
    ant = genWords(symbols, n-1)
    for x in ant:
        for y in symbols:
            l.append(x+y)
    return l


def main():
    lstA = genWords3("abc")
    print(lstA)

    lstB = genWords("abc", 3)  # should return the same words, maybe in other order
    print(lstB)
    assert sorted(lstA) == sorted(lstB)

    lstC = genWords("01", 4)  # should return all length-4 binary words
    print(lstC)

if __name__ == "__main__":
    main()

