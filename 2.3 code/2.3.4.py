n = int(input())
c = list(map(int, input().split()))
t = int(input())

for _ in range(t):
    p, dir = input().split()
    p = int(p) - 1
    if dir == "RIGHT":
        rt = p - 1
        s = c[p]//2
        c[p] -= s
        c[rt] += s
    if dir == "ACROSS":
        ac = (p + n//2) % n
        s = c[p]//2
        c[p] -= s
        c[ac] += s

c = [str(x) for x in c]
print(" ".join(c))

