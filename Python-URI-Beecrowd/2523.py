while True:
    try:
        lista_letras = list(input())
        n1 = int(input())
        letras = input().split()
        for c in range(n1):
            k = int(letras[c])
            print(lista_letras[k-1],end='')
        print()
    except EOFError:
        break
