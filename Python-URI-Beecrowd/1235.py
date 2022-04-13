n = int(input())
for c in range(n):
    s = input()
    s = s[::-1]
    s1 = []
    for c in range(len(s)//2, len(s)):
        s1.append(s[c])
    for c in range(0, len(s)//2):
        s1.append(s[c])
    s1 = ''.join(s1)
    print(s1)
