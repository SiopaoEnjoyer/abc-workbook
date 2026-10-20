n = int(input())
l = input().split()
t = int(input())

for i in range(t):
    k, x = map(int, input().split())
    k, x = k-1, x-1
    l[k], l[x] = l[x], l[k]

print(" ".join(l))