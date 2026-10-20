n = int(input())
c = [input() for _ in range(n)]
h = 1
fv = c[0].split(" ")[0]
for i in range(1, n):
    suit = c[i].split(" ")[0]
    if fv == suit:
        h += 1    
print(h)