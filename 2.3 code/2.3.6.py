n = int(input())
f = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    L, R = map(int, input().split())
    L -= 1
    nf = sorted(f[L:R])
    if len(nf) % 2 != 0:
        print(f"{nf[len(nf)//2]:.2f}")
    else:
        avg = (nf[len(nf)//2 - 1] + nf[len(nf)//2] ) / 2
        print(f"{avg:.2f}")
