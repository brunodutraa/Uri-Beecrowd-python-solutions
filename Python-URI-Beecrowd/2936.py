porcoes = [300, 1500, 600, 1000, 150]
total = 0

for c in range(5):
    convidado = int(input())
    total += convidado * porcoes[c]
print(total + 225)
