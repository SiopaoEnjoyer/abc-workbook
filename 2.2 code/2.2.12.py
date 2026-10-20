n = int(input())
l = [int(x) for x in input().split()][::-1]
e = True
for i in range(n):
    if l[i] % 2 == 0:
        print(n - i - 1)
        e = False
        break
if e:
    print("no even numbers")