n = int(input())
for k in range(n):
    entrada = input().split()
    frase1_final = []
    frase = list(entrada[0])
    frase2 = list(entrada[1])
    for c in range((len(frase) - len(frase2)), len(frase)):
        frase1_final += frase[c]
    if frase1_final == frase2:
        print('encaixa')
    else:
        print('nao encaixa')
