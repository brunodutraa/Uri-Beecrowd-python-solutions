n = int(input())
if n % 2 == 0:
    casas = n**2/2
    print(f'{casas:.0f} casas brancas e {casas:.0f} casas pretas')
else:
    casas = n**2/2
    print(f'{casas+0.5:.0f} casas brancas e {casas-0.5:.0f} casas pretas')
