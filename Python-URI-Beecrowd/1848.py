result = 0
caw = 0
while True:
    n = input()
    if n == 'caw caw':

        caw += 1

        print(result)
        result = 0

    else:
        n = n.replace('-', '0')
        n = n.replace('*','1')
        numero = int(n,2)
        result += numero
    if caw == 3:
        break
