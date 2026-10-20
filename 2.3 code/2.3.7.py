n = int(input())
f = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    L, R = map(int, input().split())
    L -= 1
    for i in range(L, R):
        f[i] += 1
f = [str(s) for s in f]
print(" ".join(f))
