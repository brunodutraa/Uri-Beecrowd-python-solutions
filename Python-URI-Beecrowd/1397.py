while True:
    av = 0
    bv = 0
    n = int(input())
    if n != 0:
        for c in range(n):
            jogo = input().split()
            a = int(jogo[0])
            b = int(jogo[1])
            if a > b:
                av += 1
            if b > a:
                bv += 1
        print(av, bv)
    else:
        break
