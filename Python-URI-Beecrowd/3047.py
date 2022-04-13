m = int(input())
a = int(input())
idade = a
b = int(input())
if idade < b:
    idade = b
c = m - (a + b)
if idade < c:
    idade = c
print(idade)
