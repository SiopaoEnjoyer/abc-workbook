n = int(input())
dominoes = []
for _ in range(n):
    domino = input().split()
    dominoes.append(domino[0])
    dominoes.append(domino[1])

d1 = dominoes[0]
d2 = dominoes[1]
d3 = dominoes[2]
d4 = dominoes[3]

p = True
a = None
b = None

if d1 == d3 or d2 == d3:
    a = d4
if d1 == d4 or d2 == d4:
    b = d3
if a is None and b is None:
    p = False
    print("NO")

if n > 2 and p:
    for i in range(4, len(dominoes)-1, 2):
        x = dominoes[i]
        y = dominoes[i+1]
        na = None
        nb = None
        if x == a or x == b:
            na = y
        if y == a or y == b:
            nb = x
        if na is None and nb is None:
            p = False
            print("NO")
            break
        a = na
        b = nb  

if p:
    print("YES")