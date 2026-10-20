n, h, k = map(int, input().split())
l = []
for i in range(n):
    x, y = map(int, input().split())
    d = 2 * (((x-h)**2 + (y-k)**2)**0.5)
    l.append(d)
big = max(l)
print(f"{big:.4f}")

