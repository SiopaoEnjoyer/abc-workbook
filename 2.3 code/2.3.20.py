m, n = map(int, input().split())
l = [0]
for _ in range(n):
    n1, n2 = map(int, input().split())
    if n1 in l and n2 in l:
        continue
    elif (n1 in l and n2 not in l):
        l.append(n2)
    elif (n2 in l and n1 not in l):
        l.append(n1)
print(len(l))