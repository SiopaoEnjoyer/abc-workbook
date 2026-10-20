n = int(input())
p = list(map(int, input().split()))
y = list(map(int, input().split()))
t = 0

for i, j in zip(p, y):
    if j <= 1960:
        continue
    elif j >= 2000:
        t += i/2
    else:
        t += i * (1.105**(2024-j))

print(f"{t:.2f}")
