n, m = map(int, input().split())
f = list(map(int, input().split()))
f = [i-1 for i in f]
v = [0] * n
for i in f:
    v[i] += 1
v = [str(x) for x in v]
print(" ".join(v))