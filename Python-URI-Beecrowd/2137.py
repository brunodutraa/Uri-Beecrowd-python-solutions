while True:
    try:
        n = int(input())
        lista = []
        for c in range(n):
            num = input()
            lista.append(num)
        lista.sort()
        for num in lista:
            print(num)
    except EOFError:
        break
