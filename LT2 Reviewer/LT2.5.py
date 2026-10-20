n, m, L, R = map(int, input().split())
x_coord = list(map(int, input().split()))
y_coord = list(map(int, input().split()))

Area = []

x_coord.insert(0, 0)
y_coord.insert(0, 0)

dx, dy = [], []

for i in range(len(x_coord)-1):
    distance = abs(x_coord[i] - x_coord[i+1])
    dx.append(distance)

for j in range(len(y_coord)-1):
    distance = abs(y_coord[j] - y_coord[j+1])
    dy.append(distance)

for a in dx:
    for b in dy:
        s = a*b
        if L <= s <= R:
            Area.append(s)

print(len(Area))