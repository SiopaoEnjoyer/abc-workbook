n = int(input())
s = list(input())
dir = ""
for i in range(n):
    if s[i] == "N":
        dir += "S"
    elif s[i] == "S":
        dir += "N"
    elif s[i] == "W":
        dir += "E"
    elif s[i] == "E":
        dir += "W"
print(dir[::-1])