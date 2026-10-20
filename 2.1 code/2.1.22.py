n = int(input())
c = [input() for _ in range(n)]
s = input()
nc = True
for i in c:
    if i.split()[-1] == s:
        print(i)
        nc = False
if nc:
    print("no cards")