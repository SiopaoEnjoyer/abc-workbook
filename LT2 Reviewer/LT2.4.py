def digit_square_sum(x):
    return sum(int(d) ** 2 for d in str(x))

n = int(input())
c = 0
while n not in (1, 42):
    n = digit_square_sum(n)
    c += 1

print(c)
print(n)