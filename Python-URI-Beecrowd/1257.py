n = int(input())
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for c in range(n):
    q = int(input())
    soma = 0
    for d in range(q):
        termo = list(input())
        for e in range(len(termo)):
            posicao = int(alfabeto.index(termo[e]))
            soma += posicao + int(e) + int(d)
    print(soma)
