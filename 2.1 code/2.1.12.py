n = int(input())
f = list(map(int, input().split()))
ma = max(f)
s = []
for i in range(n):
    if f[i] == ma:
        s.append(str(i + 1))
print(" ".join(s))