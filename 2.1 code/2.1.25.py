n = int(input())
cards = [input() for _ in range(n)]
t, b = cards[:n//2], cards[n//2:]
for i in range(n):
    if i % 2 == 0:
        print(t[i//2])
    else:
        print(b[i//2])
        