t = int(input())

n_i = 0
n_i1 = 1
s = n_i + n_i1

while s < t:
    n_i = n_i1
    n_i1 = s
    s = n_i + n_i1

print(s if s != 0 else 0)