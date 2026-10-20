s, t = map(int, input().split())

l, c = [], 0

while s < t:
    if s in l:
        print("MOVE ON")
        break
    else:
        l.append(s)
        s = s**2 - 3
        c += 1

if s >= t:
    print(c)