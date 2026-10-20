n = int(input())
p = [int(x) for x in input().split()]
o, e = [], []
for i in p:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)     
e = sorted(e)
o = sorted(o)
e = [str(x) for x in e]
o = [str(x) for x in o]

print(" ".join(o))
print(" ".join(e))
