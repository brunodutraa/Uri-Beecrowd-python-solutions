def uri(n1, n2):
    n3 = cont = 0
    while n3 < n2:
        n3 += n1
        n1 += 1
        cont += 1
    print(cont)


n1 = int(input())
while True:
    n2 = int(input())
    if n2 > n1:
        break
uri(n1, n2)
