n = int(input())
og = list(range(1, n + 1))
f1 = list(map(int, input().split()))
f3 = list(map(int, input().split()))
f2, f4, fnl = [], [], []

for i, j in zip(og, f1):
    f2.append((j, i))

f2 = sorted(f2)

for _, k in f2:
    f4.append(k)

for l in range(len(f4)):
    a = str(f3.index(f4[l]) + 1)
    fnl.append(a)

print(" ".join(fnl))