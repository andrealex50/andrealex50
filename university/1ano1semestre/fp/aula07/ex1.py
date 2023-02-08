import sys
#filename = input('Filename? ')
#filename = sys.argv[0]
d={}
with open(sys.argv[1],'r', encoding="utf-8") as file:
    for line in file:
        for letter in line:
            if letter.isalpha():
                letter = letter.lower() 
                if letter not in d.keys():
                    d[letter] = 0
                d[letter] += 1
    print(d)
            
        

        
