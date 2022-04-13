n = int(input())
for c in range(n):
    opcoes = input().split()
    op1 = opcoes[0]
    op2 = opcoes[1]
    if op1 == op2:
        print('empate')
    else:
        if op1 == 'tesoura':
            if op2 == 'papel':
                print('rajesh')
            elif op2 == 'lagarto':
                print('rajesh')
            else: #op2 == 'spock':
                print('sheldon')
        elif op1 == 'papel':
            if op2 == 'pedra':
                print('rajesh')
            elif op2 == 'spock':
                print('rajesh')
            else:
                print('sheldon')
        elif op1 == 'pedra':
            if op2 == 'lagarto':
                print('rajesh')
            elif op2 == 'tesoura':
                print('rajesh')
            else:
                print('sheldon')
        elif op1 == 'lagarto':
            if op2 == 'spock':
                print('rajesh')
            elif op2 == 'papel':
                print('rajesh')
            else:
                print('sheldon')
        elif op1 == 'spock':
            if op2 == 'tesoura':
                print('rajesh')
            elif op2 == 'pedra':
                print('rajesh')
            else:
                print('sheldon')
