n = int(input())
for i in range(n):
    s = input().split()
    if int(s[2]) % 2 == 0 and s[-1] == "even.":
        print("CORRECT")
    elif int(s[2]) % 2 != 0 and s[-1] == "odd.":
        print("CORRECT")
    else:
        print("INCORRECT")
