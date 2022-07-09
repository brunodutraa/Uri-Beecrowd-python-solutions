f, b, m = map(int, input().split())
r1, r2, r3 = map(int, input().split())
falta = 0
if r1 > f:
    falta += r1 - f
if r2 > b:
    falta += r2 - b
if r3 > m:
    falta += r3 - m
print(falta)
