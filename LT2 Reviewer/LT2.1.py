n = int(input())
c = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    L, R, x = map(int, input().split())
    ans = -1
    for i in range(L - 1, R):
        if c[i] >= x:
            ans = i + 1
            break
    print(ans)