salario = float(input())
if salario > 0 and salario <= 400:
    reajuste = salario / 100 * 15
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 15 %')
elif salario > 400 and salario <= 800:
    reajuste = salario / 100 * 12
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 12 %')
elif salario > 800 and salario <= 1200:
    reajuste = salario / 100 * 10
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 10 %')
elif salario > 1200 and salario <= 2000:
    reajuste = salario / 100 * 7
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 7 %')
elif salario > 2000:
    reajuste = salario / 100 * 4
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 4 %')
