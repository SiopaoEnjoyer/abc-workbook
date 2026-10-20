n = int(input())
c = input().split()
v, s = c[0], c[-1]
empty = True
for i in range(n-1):
    ci = input().split()
    if ci[0] != v and ci[-1] != s:
        empty = False
        print(" ".join(ci))
if empty:
    print("empty deck")