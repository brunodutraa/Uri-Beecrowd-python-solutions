while True:
    try:
        lista = []
        n = int(input())
        for c in range(n):
            tentativa = float(input())
            lista.append(tentativa)
        print(min(lista))
    except EOFError:
        break
