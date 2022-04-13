resp = 1
vit_gre = 0
vit_int = 0
grenais = 0
emp = 0
while resp == 1:
    grenais += 1
    gols = input().split()
    gre = int(gols[1])
    inter = int(gols[0])
    if inter > gre:
        vit_int += 1
    elif gre > inter:
        vit_gre += 1
    else:
        emp += 1
    resp = int(input('Novo grenal (1-sim 2-nao)\n'))
print(grenais,'grenais')
print('Inter:{}'.format(vit_int))
print('Gremio:{}'.format(vit_gre))
print('Empates:{}'.format(emp))
if vit_gre > vit_int:
    print('Gremio venceu mais')
elif vit_int > vit_gre:
    print('Inter venceu mais')
elif vit_int == 0 and vit_gre == 0:
    print('Nao houve vencedor')
