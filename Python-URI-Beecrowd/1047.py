entrada = input().split()
h1 = int(entrada[0])
m1 = int(entrada[1])
h2 = int(entrada[2])
m2 = int(entrada[3])
if h1 < h2:
    if m1 == m2:
        horas = h2 - h1
        minutos = 0
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    if m1 < m2:
        horas = h2 - h1
        minutos = m2 - m1
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    if m1 > m2:
        minutos = 60 - m1 + m2
        horas = h2 - h1 - 1
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
if h1 > h2:
    horas = 24 - (h1 - h2)
    if m1 < m2:
        minutos = m2 - m1
    if m1 > m2:
        horas = horas - 1
        minutos = 60 - m1 + m2
    if m1 == m2:
        minutos = 0
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
if h1 == h2:
    if m1 == m2:
        horas = 24
        minutos = 0
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    if m1 < m2:
        horas = 0
        minutos = m2 - m1
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    if m1 > m2:
        horas = 23
        minutos = 60 - m1 + m2
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
