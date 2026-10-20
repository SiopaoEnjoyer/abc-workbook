n, s, k = map(int, input().split())
w = list(map(int, input().split()))

k = k-1

for i in range(k):
    s = w[s-1]
    l = w[s-1]

print(f"Location: {l}")