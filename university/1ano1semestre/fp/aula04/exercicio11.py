n = int(input('Número? '))
def divisores(n):
    somadivisores = 0
    d=[]
    for i in range(1,n+1):
        if n % i == 0 and i != n:
            d.append(i)
            somadivisores += i
    if somadivisores < n:
        return (d, 'deficiente')
    elif somadivisores > n:
        return (d, 'abundante')
    else:
        return (d, 'perfeito')
    
print(divisores(n))