n = int(input('N? '))
n = n-1
def leibnizPi4(n):
    sum = 0
    while n>=0:
        pi = ((-1)**n)/(2*n+1)
        n -= 1
        sum += pi
    return sum
leibnizPi4(n)