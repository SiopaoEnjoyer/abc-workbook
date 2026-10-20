s = input()
t = 0
for i in range(1, len(s)-1, 2):
    op, number = s[i], int(s[i+1])
    if op == "-":
        t -= number
    elif op == "+":
        t += number
t = t + int(s[0])
print(t)