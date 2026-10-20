n = int(input())
w = [str(x) for x in input().split()]
s = ""
for i in range(n):
    s += f"{w[i]}::"
print(s[:-2])