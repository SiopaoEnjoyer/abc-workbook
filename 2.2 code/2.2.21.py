def mix(x, y):
    if x == "A" and y == "A":
        return "C"
    elif x == "B" and y == "B":
        return "B"
    elif x == "C" and y == "C":
        return "A"
    elif (x == "A" and y == "B") or (x == "B" and y == "A"):
        return "A"
    elif (x == "A" and y == "C") or (x == "C" and y == "A"):
        return "B"
    elif (x == "B" and y == "C") or (x == "C" and y == "B"):
        return "C"

n = int(input())
c = input().split()
for i in range(n-1):
    c[i+1] = mix(c[i], c[i+1])
print(c[-1])