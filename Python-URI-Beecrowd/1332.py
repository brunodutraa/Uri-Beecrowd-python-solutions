n = int(input())
for c in range(n):
    word = input()
    if len(word) == 3 :
        teste = list(word)
        if 'on' in word or 'ne' in word or word == 'one' or (teste[0] == 'o' and teste[2] == 'e'):
            print('1')
        elif 'tw' in word or 'wo' in word or word == 'two' or (teste[0] == 't' and teste[2] == 'o'):
            print('2')
    if len(word) == 5:
        teste = list(word)
        if 'thre' in word or 'hree' in word or teste[1] != 'h' or teste[2] != 'r' or teste[3] != 'e':
            print('3')
