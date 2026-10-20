n = int(input())
f = list(map(int, input().split()))
R, k = map(int, input().split())
for i in range(R-1):
    f[i] = k
print(" ".join([str(x) for x in f]))