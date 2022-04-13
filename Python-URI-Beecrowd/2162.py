n = input()
lista = input().split()
int_list = [int(t) for t in lista]
maior = int_list[0]
pico = False
if int_list[0] < int_list[1]:
    pico = True
vitoria = True
if int_list[0] == int_list[1]:
    print(0)
    vitoria = False
else:
    for c in range(2, len(int_list)):
        if pico:
            if int_list[c] >= int_list[c - 1]:
                print(0)
                vitoria = False
                break

            else:
                pico = False
        elif not pico:
            if int_list[c] <= int_list[c - 1]:
                print(0)
                vitoria = False
                break

            else:
                pico = True
    if vitoria:
        print(1)
