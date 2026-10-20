n = int(input())
temp = [int(x) for x in input().split()]
L, R = map(int, input().split())
c = True
for i in range(L-1, R):
    if temp[i] > 50:
        print(i + 1)
        c = False
        break
if c:
    print("no reaction")