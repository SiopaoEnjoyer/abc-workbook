n = int(input())
f = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    L, R = map(int, input().split())
    L -= 1
    print(max(f[L:R]))