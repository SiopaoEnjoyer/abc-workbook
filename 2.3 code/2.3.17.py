n = int(input())
o = [int(x) for x in input().split()]
a = [0] * (n + 2) #padding so that u don't have to do if statements for i == 0 or i == n-1

for i in o:
    used = (a[i-1], a[i+1])
    k = 1
    while k in used:
        k += 1
    a[i] = k
print(*a[1:n-1])