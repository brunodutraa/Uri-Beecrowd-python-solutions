while True:
    try:
        n = int(input())
        if n == 2:
            break
        mod = n % 100
        if mod == 0:
            sec = n / 100
        else:
            sec = n // 100 + 1
        print(f'{sec:.0f}')
    except EOFError:
        break
