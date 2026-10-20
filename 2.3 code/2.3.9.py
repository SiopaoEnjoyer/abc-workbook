n = int(input())
f = list(map(int, input().split()))
t = int(input())

def operator(s, f):
    if s == "INCREASE":
        L, R, k = map(int, input().split())
        L -= 1
        for i in range(L, R):
            f[i] = f[i] + k
    elif s == "SORT":
        sign = input()
        if sign == "+":
            f.sort()
        elif sign == "-":
            f.sort(reverse=True)
    elif s == "AVERAGE":
        L, R = map(int, input().split())
        L -= 1
        print(f"{ (sum(f[L:R])) / len(f[L:R]):.2f}")
    elif s == "COUNT":
        L, R, k = map(int, input().split())
        L -= 1
        c = 0
        for i in range(L, R):
            if f[i] <= k:
                c += 1
        print(c)

for _ in range(t):
    operator(input(), f)