idadeEmDias = int(input())
anos = (idadeEmDias // 365)
meses = (idadeEmDias % 365) // 30
dias =  (idadeEmDias % 365) % 30
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
