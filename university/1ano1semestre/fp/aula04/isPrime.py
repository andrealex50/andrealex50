#n = float(input('Número?: '))

def isPrime(n):
    if n%2 != 0 and n%3 != 0 and n != 1:
        print(n, 'é numero primo')
    elif n in range(2,4):
        print(n, 'é numero primo')
    else:
        print(n, 'é numero não primo')

n = 1
while n < 101:
    isPrime(n)
    n += 1
