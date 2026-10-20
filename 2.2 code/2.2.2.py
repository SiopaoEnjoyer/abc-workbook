n = int(input())
scores = [int(x) for x in input().split()]
avg = sum(scores) / n
a, b = 0, 0
for i in range(n):
    if avg > scores[i]:
        a += 1
    elif avg < scores[i]:
        b += 1
print(f"{a} scored below average")
print(f"{b} scored above average")
    
