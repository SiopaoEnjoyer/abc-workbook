n = int(input())
f = list(map(int, input().split()))
L, R = map(int, input().split())
L -= 1
for i in range(L, R):
    f[i] += 1
print(" ".join([str(x) for x in f]))