def shorten(line):
    maiusculas = ''
    for car in line:
        if car.isupper():
            maiusculas += car
    return maiusculas

print(shorten("Universidade de Aveiro"))
print(shorten("United Nations Organization"))