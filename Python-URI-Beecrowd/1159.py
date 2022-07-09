while True:
    pares = soma = 0
    n = int(input())
    if n == 0:
        break
    else:
        while pares < 5:
            if n % 2 == 0:
                soma += n
                pares += 1
            n += 1
        print(soma)