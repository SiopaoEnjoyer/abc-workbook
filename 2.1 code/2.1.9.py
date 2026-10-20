n = int(input())
print(" ".join(str(n - 5 if n > 5 else n) for n in map(int, input().split())))