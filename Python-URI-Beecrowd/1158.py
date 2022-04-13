soma = 0
qt_repete = int(input())
for c in range(qt_repete):
    teste = input().split()
    x = int(teste[0])
    y = int(teste[1])
    if x % 2 == 0:
        x2 = x
        x2 += 1
        x += 1
        for conta_impares in range(y-1):
            x = x + 2
            soma += x
    else:
        x2 = x
        for conta_impares in range(y - 1):
            x = x + 2
            soma += x
    print(soma + x2)
    soma = 0
