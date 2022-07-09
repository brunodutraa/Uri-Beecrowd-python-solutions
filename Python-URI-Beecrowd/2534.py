while True:
    try:
        notas = []
        habitantes, consultas = map(int, input().split())
        for c in range(habitantes):
            notas.append(int(input()))
        notas.sort(reverse=True)
        for c in range(consultas):
            p = int(input())
            print(notas[p - 1])

    except EOFError:
        break
