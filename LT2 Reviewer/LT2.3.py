n = int(input())
p = list(map(int, input().split()))
l = [0] * n
cur = list(range(n))
mx = p.index(max(p))

while len(cur) > 1:
    nxt = []
    for i in range(0, len(cur), 2):
        a, b = cur[i], cur[i + 1]
        winner = a if p[a] > p[b] else b
        l[a] += 1
        l[b] += 1
        nxt.append(winner)
    cur = nxt

l = [str(x) for x in l]
l[mx] = "CHAMP"
print(" ".join(l))