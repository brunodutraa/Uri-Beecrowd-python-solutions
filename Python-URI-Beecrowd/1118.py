notas = 0
media = 0
while True:
    while notas < 2:
        nota = float(input())
        if not 0 <= nota <= 10:
            print('nota invalida')
        else:
            media = nota + media
            notas = notas + 1
    print('media = {:.2f}'.format(media / 2))
    notas = 0
    media = 0

    resp = 0
    while resp != 1 and resp != 2:
        print('novo calculo (1-sim 2-nao)')
        resp = int(input())
    if resp == 2:
        break
