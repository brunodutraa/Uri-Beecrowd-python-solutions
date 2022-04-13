while True:
    try:
        qtd = int(input())
        lesmas = input().split()
        maior = 0
        for lesma in lesmas:
            if int(lesma) > maior:
                maior = int(lesma)
        if maior < 10:
            print(1)
        elif 10 <= maior < 20:
            print(2)
        elif maior >= 20:
            print(3)
    except EOFError:
        break
