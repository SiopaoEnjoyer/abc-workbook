n, r = map(int, input().split())
a = list(map(int, input().split()))

def A(x):
    smallest = abs(x - a[0])
    for v in a:
        distance = abs(x - v)
        if distance < smallest:
            smallest = distance
    return smallest

total = 0
for i in range(r):
    total += A(i) + A(i + 1)

print(total // 2)