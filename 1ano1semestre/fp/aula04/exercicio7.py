def medianumeros():
    media = 0
    total = 0
    i = 0
    while True:
        n=input('Número?: ')
        i += 1
        if n=='': break
        v = float(n)
        total += v
        media = total/i
    return media

def main():
   media = medianumeros() 
   print(media)

if __name__ == "__main__":
    main()
