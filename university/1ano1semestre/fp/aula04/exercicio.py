n = int(input('n: '))
reverse = 0
while n > 0:
    resto = n % 10
    reverse = reverse*10 + resto
    n = n // 10
print(reverse)


    

    


