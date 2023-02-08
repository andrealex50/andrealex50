
# Calcula o factorial de n, baseado na recorrencia n! = n*(n-1)!.
# Mas não termina!  Detete a causa e corrija o erro.
def fact(n):
    if n==1:
        return 1
    r = n*fact(n-1)
    return r



# Calcula o maximo divisor comum entre a e b.
# Baseia-se no algoritmo de Euclides.
# Mas não termina!  Detete a causa e corrija o erro.
def gcd(a, b):
    while a != b:
        if a<b:
            b = b-a
        else:
            a=a-b
    return a


def main():
    n = int(input('Número: '))
    print( fact(n) )
    print( fact(4) )    # 24
    print( fact(5) )    # 120
    a = int(input('Número 1> '))
    b = int(input('Número 2> '))
    print(gcd(a, b))
    x = 2*27*53*61
    y = 2*2*17*23*53
    print(x, y, gcd(x, y))
    assert gcd(x, y) == 2*53

if __name__ == "__main__":
    main()

