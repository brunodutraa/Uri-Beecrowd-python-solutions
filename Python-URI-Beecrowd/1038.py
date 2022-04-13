lanche = input().split()
cod = int(lanche[0])
qt = int(lanche[1])
if cod == 1:
    print('Total: R$ {:.2f}'.format(qt * 4))
if cod == 2:
    print('Total: R$ {:.2f}'.format(qt * 4.5))
if cod == 3:
    print('Total: R$ {:.2f}'.format(qt * 5))
if cod == 4:
    print('Total: R$ {:.2f}'.format(qt * 2))
if cod == 5:
    print('Total: R$ {:.2f}'.format(qt * 1.5))
