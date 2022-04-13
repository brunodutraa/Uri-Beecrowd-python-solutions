lista = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
quantidade = int(input())
for k in range(quantidade):
    ns = input()
    nslist = list(ns)
    tam = int(len(ns))
    soma = 0
    for c in range(tam):
        if nslist[c] == '1':
            soma = soma + lista[0]
        elif nslist[c] == '2':
            soma = soma + lista[1]
        elif nslist[c] == '3':
            soma = soma + lista[2]
        elif nslist[c] == '4':
            soma = soma + lista[3]
        elif nslist[c] == '5':
            soma = soma + lista[4]
        elif nslist[c] == '6':
            soma = soma + lista[5]
        elif nslist[c] == '7':
            soma = soma + lista[6]
        elif nslist[c] == '8':
            soma = soma + lista[7]
        elif nslist[c] == '9':
            soma = soma + lista[8]
        else:
            soma = soma + lista[9]
    print(soma, 'leds')
