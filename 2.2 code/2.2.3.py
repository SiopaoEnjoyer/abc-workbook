n = int(input())
c = [input() for _ in range(n)]
h = 0
for i in range(n):
    suit = c[i].split(" ")[-1]
    if suit == "Hearts":
        h += 1
print(h)