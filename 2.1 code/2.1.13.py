n = int(input())
f = list(map(int, input().split()))
s = []
for i in range(n):
    if i == 0:
        if f[i] > f[i+1]:
            s.append(str(i+1))
    elif i == n - 1:
        if f[i] > f[i-1]:
            s.append(str(i+1))
    else:
        if f[i] > f[i+1] and f[i] > f[i-1]:
            s.append(str(i+1))
if len(s) == 0:
    print("none")
else:
    print(" ".join(s))
