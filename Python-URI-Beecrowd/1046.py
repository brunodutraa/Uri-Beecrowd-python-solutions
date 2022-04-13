entrada = input().split()
h1 = int(entrada[0])
h2 = int(entrada[1])
if h1 < h2:
    horas = h2 - h1
    print('O JOGO DUROU {} HORA(S)'.format(horas))
if h1 > h2:
    horas = 24 - (h1 - h2)
    print('O JOGO DUROU {} HORA(S)'.format(horas))
if h1 == h2:
    print('O JOGO DUROU 24 HORA(S)')
