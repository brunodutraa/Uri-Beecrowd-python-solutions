n = int(input())
for c in range(n):
    pot = input().split()
    result = int(pot[0]) ** int(pot[1])
    print(len(str(result)))
