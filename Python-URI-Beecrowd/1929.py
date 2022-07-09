a, b, c, d = map(int, input().split())

combinacoes = ([a, b, c], [a, b, d], [a, c, d], [b, c, d])
forma = False

for combinacao in combinacoes:
    aux = []
    for medida in combinacao:
        if medida is not max(combinacao):
            aux.append(medida)
        if sum(aux) > max(combinacao):
            print('S')
            forma = True
            break
    if forma:
        break

if not forma:
    print('N')
