while True:
    try:
        n = input(). split()
        soma = 0
        lista = list(n[1])
        for numero in lista:
            soma += int(numero)
        print(soma, end=' ')
        if soma % 3 == 0:
            print('sim')
        else:
            print('nao')
    except EOFError:
        break
