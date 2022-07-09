while True:
    try:
        n = int(input())
        votos = input()
        v0 = votos.count('0')
        v1 = votos.count('1')
        if v1 >= (n / 3 * 2):
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break