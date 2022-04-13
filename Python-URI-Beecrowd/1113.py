while True:
    valores = input().split()
    if valores[0] == valores[1]:
        break
    else:
        if int(valores[0]) > int(valores[1]):
            print('Decrescente')
        else:
            print('Crescente')
