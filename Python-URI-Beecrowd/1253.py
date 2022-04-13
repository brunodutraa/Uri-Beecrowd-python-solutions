n = int(input())
for t in range(n):
    codigo = list(input())
    quantas_pulou = int(input())
    afbt = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for c in range(len(codigo)):
        ind = afbt.index(codigo[c])
        codigo[c] = afbt[ind - quantas_pulou]
    print(''.join(codigo))
