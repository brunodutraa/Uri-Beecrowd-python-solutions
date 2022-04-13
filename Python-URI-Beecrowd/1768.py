while True:
    try:
        t = int(input())
        inicio = 1
        espaco = t // 2
        if t % 2 == 0:
            espaco -= 1
        while inicio <= t:
            print(espaco * ' ', end='')
            print('*' * inicio)
            inicio += 2
            espaco -= 1

        espaco = t//2
        if t % 2 == 0:
            espaco -= 1
        print((' ' * espaco) + '*')
        print(' ' * (espaco - 1) + '***')
        print()
    except EOFError:
        break
