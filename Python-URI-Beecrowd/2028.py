caso = 1
cont = 1
while True:
    try:
        n = int(input())
        numeros = 1
        for c in range(n, 0, -1):
            numeros += c
        if numeros == 1:
            print(f'Caso {caso}: {numeros} numero')
            print(0)
        else:
            print(f'Caso {caso}: {numeros} numeros')
            print(0,end=' ')
        if n >= 1:
            for c in range(1, n+1):
                for d in range(c):
                    if cont == numeros-1:
                        print(c)
                    else:
                        print(c, end=' ')
                    cont += 1
        caso += 1
        print('')
        cont = 1
    except EOFError:
        break
