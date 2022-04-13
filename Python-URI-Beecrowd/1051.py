salario = float(input())
if salario >= 0 and salario <= 2000:
    print('Isento')
elif salario > 2000 and salario <= 3000:
    print('R$ {:.2f}'.format((salario - 2000) * 0.08))
elif salario > 3000 and salario <= 4500:
    ir = (1000 / 100 * 8) + ((salario - 3000) * 0.18)
    print('R$ {:.2f}'.format(ir))
elif salario > 4500:
    ir = (1000 / 100 * 8) + 1500 * 0.18 + ((salario - 4500) * 0.28)
    print('R$ {:.2f}'.format(ir))
