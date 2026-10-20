n = int(input())
l = list(map(int, input().split()))
a = []
for i in range(n-1):
    if l[i] > l[i+1]:
        a.append(f"-{l[i]-l[i+1]}")
    elif l[i] < l[i+1]:
        a.append(f"+{l[i+1]-l[i]}")
    elif l[i] == l[i+1]:
        a.append("0")
print(" ".join(a))