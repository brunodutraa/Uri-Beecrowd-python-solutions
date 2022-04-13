s = 0
n = int(input())
resp = input().split()
for c in range(5):
    if int(resp[c]) == n:
        s += 1
print(s)
