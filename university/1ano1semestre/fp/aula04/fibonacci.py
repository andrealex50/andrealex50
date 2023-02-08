n = int(input('Termo? '))

def fibonacci(n):
    f0 = 0
    f1 = 1
    for i in range(0, n-1):
        valor = f0 + f1
        f0 = f1
        f1 = valor
    return f0

print(fibonacci(n))

