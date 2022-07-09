while True:
    try:
        soma = 1
        jutsu = 0
        n = int(input())
        while soma < n:
            soma *= 2
            jutsu += 1
        print(jutsu)
    except EOFError:
        break
