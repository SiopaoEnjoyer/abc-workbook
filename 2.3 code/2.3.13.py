dir = input()
x, y = 0, 0
for i in range(len(dir)):
    if dir[i] == "U":
        y += 1
        print(x, y)
    if dir[i] == "D":
        y -= 1
        print(x, y)
    if dir[i] == "R":
        x += 1
        print(x, y)
    if dir[i] == "L":
        x -= 1
        print(x, y)