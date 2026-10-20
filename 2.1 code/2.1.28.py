n = int(input())
s = list(input())
new = ""
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        new += s[i]
new = f"{new}{s[-1]}"
print(new)