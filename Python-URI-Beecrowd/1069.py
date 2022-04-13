n = int(input())
for c in range(n):
    diamante = 0
    frase = input()
    frase = frase.replace('.','')
    while '<>' in frase:
        counter = frase.count('<>')
        diamante = diamante + counter
        frase = frase.replace('<>','')
    print(diamante)
