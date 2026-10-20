n = int(input())
f, f_n = list(map(int, input().split())), []
mi, ma = min(f), max(f)
for i in range(n):
    if f[i] == mi:
        f_n.append(ma)
    else:
        f_n.append(f[i])
print(" ".join([str(x) for x in f_n]))