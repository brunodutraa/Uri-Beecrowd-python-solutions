inn = out = 0
n = int(input())
for c in range(n):
    num = int(input())
    if 10 <= num <= 20:
        inn += 1
    else:
        out += 1
print(f'{inn} in\n{out} out')
