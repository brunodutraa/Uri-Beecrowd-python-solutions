leitura_arquivo = True
while leitura_arquivo:
    try:
        fatores = input().split()
        f1 = int(fatores[0])
        f2 = int(fatores[1])
        fat1 = f1
        fat2 = f2
        if f1 == 0:
            fat1 = 1
        else:
            for c in range(f1 - 1, 0, -1):
                fat1 = fat1 * c
        if f2 == 0:
            fat2 = 1
        else:
            for c in range(f2 - 1, 0, -1):
                fat2 = fat2 * c
        soma = fat1 + fat2
        print(soma)
    except EOFError:
        leitura_arquivo = False
