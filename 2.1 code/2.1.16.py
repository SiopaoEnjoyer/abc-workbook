n = int(input())
f = list(map(int, input().split()))
g = list(map(int, input().split()))
n = []
for i, j in zip(f, g):
    n.append(i + j)
print(" ".join([str(x) for x in n]))
