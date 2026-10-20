n, t = map(int, input().split())
c = 0

while n < t:
    n += n*0.01
    n = int(n)
    c += 1

print(c)