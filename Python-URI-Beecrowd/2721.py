bolas = list(map(int, input().split()))
renas = ('Rudolph', 'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen')
total = sum(bolas)
print(renas[total % 9])
