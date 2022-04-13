def arredondar(num):
    return float('%g' % (num))

moedas1 = moedas50 = moedas25 = moedas10 = moedas5 = moedas01 = 0
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0
saldo = float(input())
print('NOTAS:')
if saldo // 100 > 0:
    notas100 = saldo // 100
    saldo -= notas100 * 100
print(f'{notas100:.0f} nota(s) de R$ 100.00')
if saldo // 50 > 0:
    notas50 = saldo // 50
    saldo -= notas50 * 50
print(f'{notas50:.0f} nota(s) de R$ 50.00')
if saldo // 20 > 0:
    notas20 = saldo // 20
    saldo -= notas20 * 20
print(f'{notas20:.0f} nota(s) de R$ 20.00')
if saldo // 10 > 0:
    notas10 = saldo // 10
    saldo -= notas10 * 10
print(f'{notas10:.0f} nota(s) de R$ 10.00')
if saldo // 5 > 0:
    notas5 = saldo // 5
    saldo -= notas5 * 5
print(f'{notas5:.0f} nota(s) de R$ 5.00')
if saldo // 2 > 0:
    notas2 = saldo // 2
    saldo -= notas2 * 2
print(f'{notas2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
if saldo >= 1:
    saldo -= 1
    moedas1 = 1
print(f'{moedas1:.0f} moeda(s) de R$ 1.00')
if saldo >= 0.5:
    moedas50 = 1
    saldo -= 0.5
print(f'{moedas50:.0f} moeda(s) de R$ 0.50')
if saldo >= 0.25:
    moedas25 = 1
    saldo -= 0.25
print(f'{moedas25:.0f} moeda(s) de R$ 0.25')
if saldo >= 0.10:
    moedas10 = saldo // 0.1
    saldo -= 0.10 * moedas10
print(f'{moedas10:.0f} moeda(s) de R$ 0.10')
if saldo >= 0.05:
    moedas5 = 1
    saldo -= 0.05
print(f'{moedas5:.0f} moeda(s) de R$ 0.05')
moedas01 = saldo // 0.01
saldo -= moedas01 * 0.01
saldo = arredondar(saldo)
if saldo >= 0:
    moedas01 += saldo // 0.01
    saldo -= moedas01 * 0.01
print(f'{moedas01:.0f} moeda(s) de R$ 0.01')
