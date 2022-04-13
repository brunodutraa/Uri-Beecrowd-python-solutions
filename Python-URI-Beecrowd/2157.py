n = int(input())
for c in range(n):
    lista = []
    rng = input().split()
    a = int(rng[0])
    b = int(rng[1])
    for d in range(a, b+1):
        lista.append(str(d))

    lista_str = ''.join(lista)

    lista2_str = lista_str[::-1]
    print(lista_str,end='')
    print(lista2_str)
