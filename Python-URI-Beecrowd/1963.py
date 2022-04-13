valor = input().split()
v_ant = float(valor[0])
v_dep = float(valor[1])
aumento = ((v_dep - v_ant) / v_ant) * 100
print('{:.2f}%'.format(aumento))
