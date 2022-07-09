while True:
    try:
        n, a_min, a_max = map(int, input().split())
        total = 0
        for c in range(n):
            altura = int(input())
            if a_min <= altura <= a_max:
                total += 1
        print(total)
    except EOFError:
        break
