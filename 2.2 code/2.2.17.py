s = list(input())
a, b = s.index("a"), s.index("b")
L, R = min(a, b), max(a, b)
ast = R - L - 1
print("".join(s[:L+1]) + "*"*ast + "".join(s[R:]))