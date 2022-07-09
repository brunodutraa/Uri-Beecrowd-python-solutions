centenas = {'C':100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900}
dezenas = {'X':10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90}
unidades = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}

n = int(input())

if n // 100 > 0:
    c = n // 100 * 100
    n -= c
    for chave, valor in centenas.items():
        if valor == c:
            print(chave, end='')
if n // 10 > 0:
    d = n // 10 * 10
    n -= d
    for chave, valor in dezenas.items():
        if valor == d:
            print(chave, end='')
if n > 0:
    for chave, valor in unidades.items():
        if valor == n:
            print(chave, end='')
print('')
