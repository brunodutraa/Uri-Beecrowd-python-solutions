bolas = int(input())
galhos = int(input())

esperado = galhos // 2 - bolas
if esperado <= 0:
    print('Amelia tem todas bolinhas!')
else:
    print(f'Faltam {esperado} bolinha(s)')
