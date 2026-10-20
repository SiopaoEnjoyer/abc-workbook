n = int(input())
f = ["Jack", "Queen", "King"]
l = []
nc = True
for _ in range(n):
    l.append(input())
for j in range(n-1):
    c = l[j].split()
    cv = c[0]
    if cv in f:
        print(l[j+1])
        nc = False
if nc:
    print("no cards")
    