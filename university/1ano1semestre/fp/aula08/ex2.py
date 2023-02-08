file_name='names.txt'
def processfile(file_name):
    d = {}
    with open(file_name,'r') as file:
        for line in file:
            names = line.strip().split()
            primeiro_nome = names[0]
            apelido = names[-1]
        if apelido not in d:
            d[apelido]=set()
        d[apelido].add(primeiro_nome)
        return d

processfile(file_name)


    
  
       

        

         



        



        


