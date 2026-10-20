n = int(input())
c = [input() for _ in range(n)]
h = 0
f = ["King", "Jack", "Queen"]
for i in range(n):
    suit = c[i].split(" ")[0]
    if suit in f:
        h += 1
print(h)