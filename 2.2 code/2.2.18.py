l = [str(x) for x in input().split()]
t = int(l[0])
m = 0
a = False
names = []
for _ in range(t):
    info = [str(x) for x in input().split()]
    if info[1] == l[1]:
        m += 1
        names.append(info[0])
        a = True
    if m > 1:
        a = False
        break
if a:
    print(names[0])
else:
    print("no winner")
