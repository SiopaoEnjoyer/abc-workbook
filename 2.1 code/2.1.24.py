n = int(input())
cards = [input() for _ in range(n)]
L, R = map(int, input().split())
L -= 1
new_cards = cards[L:R] + cards[:L] + cards[R:]
for i in new_cards:
    print(i)