n = int(input())
cards = [input() for _ in range(n)]
c, s, h, d = [], [], [], []
for card in cards:
    if card.split()[-1] == "Clubs":
        c.append(card)
    if card.split()[-1] == "Spades":
        s.append(card)
    if card.split()[-1] == "Hearts":
        h.append(card)
    if card.split()[-1] == "Diamonds":
        d.append(card)
for i in c:
    print(i)
for i in d:
    print(i)
for i in h:
    print(i)
for i in s:
    print(i)



