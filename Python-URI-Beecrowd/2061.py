n = input().split()
inicial = int(n[0])
interacao = int(n[1])
for c in range(interacao):
    i = input()
    if i == 'fechou':
        inicial += 1
    else:
        inicial -= 1
print(inicial)
