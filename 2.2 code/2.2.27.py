n = int(input())
distance = sorted(list(map(int, input().split())))
power = sorted(list(map(int, input().split())))
a = True
for d, p in zip(distance, power):
    if p >= d:
        continue
    else:
        a = False
        print("NO")
        break

if a:
    print("YES")

