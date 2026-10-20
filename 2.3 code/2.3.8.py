n = int(input())
f = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    L, R, k = map(int, input().split())
    L -= 1
    for i in range(L, R):
        if f[i] >= k:
            continue
        elif f[i] < k:
            f[i] = k
f = [str(s) for s in f]
print(" ".join(f))