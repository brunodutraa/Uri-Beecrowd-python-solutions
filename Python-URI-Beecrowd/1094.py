coelhos = ratos = sapos = 0
n = int(input())
for c in range(n):
    cobaia = input().split()
    if cobaia[1] == 'C':
        coelhos += int(cobaia[0])
    elif cobaia[1] == 'R':
        ratos += int(cobaia[0])
    elif cobaia[1] == 'S':
        sapos += int(cobaia[0])
total = coelhos + ratos + sapos
porcento_coelhos = coelhos / total * 100
porcento_ratos = ratos / total * 100
porcento_sapos = sapos / total * 100
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {porcento_coelhos:.2f} %')
print(f'Percentual de ratos: {porcento_ratos:.2f} %')
print(f'Percentual de sapos: {porcento_sapos:.2f} %')
