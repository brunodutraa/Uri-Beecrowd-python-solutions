n = int(input())
for c in range(n):
    frase = input().split()
    num = input().split()
    soma = int(num[0]) + int(num[1])
    if frase.index('PAR') == 1:
        par = frase [0]
        impar = frase[2]
    else:
        par = frase[2]
        impar = frase[0]

    if soma % 2 == 0:
        print(par)
    else:
        print(impar)
