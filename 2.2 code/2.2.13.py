n = int(input())
val = [int(x) for x in input().split()]
total = [int(x) for x in input().split()]
c = 0
for v, t in zip(val, total):
    c += v*t
print(c)


