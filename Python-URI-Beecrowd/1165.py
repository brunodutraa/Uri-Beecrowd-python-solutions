n = int(input())
for c in range(n):
    primo = True
    num = int(input())
    for f in range(2, num):
        if num % f == 0:
            primo = False
    if primo:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
