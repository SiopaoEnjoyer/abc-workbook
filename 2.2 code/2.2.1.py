a, b = input().split()
words = [str(s) for s in input().split()]
c = 0
for i in range(int(a)):
    if words[i][0] == b:
        c += 1
print(c)