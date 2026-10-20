n = int(input())
f = list(map(int, input().split()))
L, R = map(int, input().split())
L -= 1
g = list(map(int, input().split()))
f_i = f[L:R]
f_i = [a + b for a, b in zip(f_i, g)]
f = [str(x) for x in f]
f_i = [str(x) for x in f_i]
print(" ".join(f[:L] + f_i + f[R:]))
