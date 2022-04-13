while True:
    num = input().split()
    if num[0] == '0' and num[1] == '0':
        break

    soma = int(num[0]) + int(num[1])
    numstr = str(soma)
    lista = []
    if '0' not in numstr:
        print(numstr)
    else:
        for numero in numstr:
            if numero != '0':
                lista.append(numero)
        numero = int(''.join(lista))
        print(numero)
