len_mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    try:
        total = falta = 0
        mes, dia = map(int, input().split())
        if mes == 12 and dia > 23:
            if dia == 24:
                print('E vespera de natal!')
            elif dia == 25:
                print('E natal!')
            elif dia > 25:
                print('Ja passou!')
        else:
            for c in range(mes):
                total += len_mes[c]
            total += dia
            falta = 360 - total
            print(f'Faltam {falta} dias para o natal!')
    except EOFError:
        break
