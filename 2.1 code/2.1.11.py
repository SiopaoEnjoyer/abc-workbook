n = int(input())
f = list(map(int, input().split()))
f_n = []
for i in range(n):
    if i == 0:
        if f[i] > f[i+1]:
            f_n.append(f[i] - 2)
        else:
            f_n.append(f[i])
    elif i == n-1:
        if f[i] > f[i-1]:
            f_n.append(f[i] - 2)
        else:
            f_n.append(f[i])
    else:
        if f[i] > f[i+1] and f[i] > f[i-1]:
            f_n.append(f[i] - 2)
        else:
            f_n.append(f[i])
print(" ".join([str(x) for x in f_n]))