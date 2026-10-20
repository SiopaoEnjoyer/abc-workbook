n = int(input())
l = []
for i in range(n):
    l.append(input())
l[0], l[-1] = l[-1], l[0]
for i in l:
    print(i)
