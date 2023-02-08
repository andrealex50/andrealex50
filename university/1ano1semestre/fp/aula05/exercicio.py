def readlst():
    print("Insert numbers after '>' (empty line to quit)")
    lst = []
    while True:
        line = input("> ")
        if line=="": break
        if line.isdigit():
            lst.append(int(line))
        else:
            lst.append(str(line))
    return lst
lista = readlst()

def calculate_reverse_int(n):
    reverse = 0
    while n > 0:
       resto = n % 10
       reverse = reverse*10 + resto
       n = n // 10
    print(reverse)

def calculate_reverse_string(s):
    return s[::-1]

lista_output = []
