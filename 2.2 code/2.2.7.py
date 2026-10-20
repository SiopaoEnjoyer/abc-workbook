n = int(input())
words = [(str(s))[0] for s in input().split()]
l = words[0]
same = True
for i in range(n):
    if words[i] != l:
        print("Invalid")
        same = False
        break
if same:
    print(l)