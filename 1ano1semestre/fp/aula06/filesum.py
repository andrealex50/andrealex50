from tkinter import filedialog
import os
print(os.getcwd())

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    name = input("File? ")                                  #A
    #name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(name):
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    soma = 0
    with open(name,'r') as reader:
        for line in reader:
            print(line)
            soma += float(line)
        return soma

if __name__ == "__main__":
    main()

