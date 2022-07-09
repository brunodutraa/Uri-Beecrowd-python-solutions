n1 = int(input())
for c in range(n1):
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        binario = list()
        while n != 0 :
            binario.append(n % 2)
            n = n // 2
        binario = binario[::-1]
        contador = 0
        maior = []
        tamanho = len(binario) -1
        for ind, num in enumerate(binario):
            if num == 1:
                contador += 1
            elif num == 0:
                maior.append(contador)
                contador = 0
            if ind == tamanho:
                maior.append(contador)
        print(max(maior))
