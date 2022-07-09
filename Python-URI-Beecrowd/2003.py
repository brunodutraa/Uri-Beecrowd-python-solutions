while True:
    try:
        h = input().split(':')
        atraso = 0
        if int(h[0]) < 7:
            print(f'Atrasso maximo: {atraso}')
        elif int(h[0]) == 7 and int(h[1]) == 0:
            print(f'Atrasso maximo: {atraso}')
        else:
            minutos = int(h[1])
            horas = (int(h[0]) + 1) - 8
            atraso = minutos + (horas * 60)
            print(f'Atraso maximo: {atraso}')
    except EOFError:
        break
