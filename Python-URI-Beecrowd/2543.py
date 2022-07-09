while True:
    try:
        tot = 0
        n, cod = map(int, input().split())
        for c in range(n):
            cod2, game = map(int, input().split())
            if cod2 == cod:
                if game == 0:
                    tot += 1
        print(tot)
    except EOFError:
        break
