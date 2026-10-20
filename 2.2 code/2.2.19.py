n = int(input())
d = [int(x) for x in input().split()]
l = []
for i in range(n):
    if d[i] != 0:
        l.append(d[i])
print(min(l))