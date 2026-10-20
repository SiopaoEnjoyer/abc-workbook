v, t = map(int, input().split())

x = 215 
for _ in range(t):
    x = (512 * x + 227) % 2027

k = 0
while x != v:
    x = (512 * x + 227) % 2027
    k += 1

print(k)