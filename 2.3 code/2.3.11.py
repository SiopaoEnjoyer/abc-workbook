n, m = map(int, input().split())
f = [0] * n

for _ in range(m):
    f1, f2 = map(int, input().split())
    f1, f2 = f1-1, f2-1
    f[f1], f[f2] = f[f1] + 1, f[f2] + 1
f = [str(s) for s in f]
print(" ".join(f))