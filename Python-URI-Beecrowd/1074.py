n = int(input())
for c in range(n):
    num = int(input())
    if num == 0:
        print('NULL')
    else:
        if num % 2 == 0:
            if num > 0:
                print('EVEN POSITIVE')
            else:
                print('EVEN NEGATIVE')
        if num % 2 != 0:
            if num > 0:
                print('ODD POSITIVE')
            else:
                print('ODD NEGATIVE')
