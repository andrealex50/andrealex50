tempo = int(input('Tempo em Segundos? '))
m1 = tempo // 60
s = tempo % 60
h = m1 // 60
m = m1 % 60
print("{:02d}:{:02d}:{:02d}".format(h, m, s))

