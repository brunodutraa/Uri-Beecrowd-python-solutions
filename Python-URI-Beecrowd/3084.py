while True:
    try:
        graus = input().split()
        h = int(graus[0]) // 30
        m = int(graus[1]) // 6
        if h < 10 > m:
            print(f'0{h}:0{m}')
        elif h < 10:
            print(f'0{h}:{m}')
        elif m < 10:
            print(f'{h}:0{m}')
        else:
            print(f'{h}:{m}')
    except EOFError:
        break
