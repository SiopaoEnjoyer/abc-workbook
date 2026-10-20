word = list(input())
n = int(input())

for _ in range(n):
    k, x = input().split()
    word[int(k) - 1] = x

print("".join(word))