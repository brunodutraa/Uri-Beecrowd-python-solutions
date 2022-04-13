final = 0
cod = ['1001', '1002', '1003', '1004', '1005']
preco = [1.5, 2.5, 3.5, 4.5, 5.5]
quantidade = int(input())
for k in range(quantidade):
    cod_qt = input().split()
    codigo = cod_qt[0]
    quant = cod_qt[1]
    posicao = cod.index(codigo)
    precofinal = float(quant) * float(preco[posicao])
    final = final + precofinal
print('{:.2f}'.format(final))
