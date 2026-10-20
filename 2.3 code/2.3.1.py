n = int(input().split()[-1])
t = int(input())

for i in range(t):
    st = input().split()
    a = int(st[-1])
    if st[0] == "FINISH":
        n = n - a
    elif st[0] == "ASSIGN":
        n = n + a
print(n)