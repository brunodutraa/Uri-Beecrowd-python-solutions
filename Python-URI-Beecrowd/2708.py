jipes = vuelta = salida = 0
while True:
    move = input().split()
    if move == ['ABEND']:
        break
    if move[0] == 'SALIDA':
        salida += int(move[1])
        jipes += 1
    elif move[0] == 'VUELTA':
        vuelta += int(move[1])
        jipes -= 1
print(salida - vuelta)
print(jipes)
