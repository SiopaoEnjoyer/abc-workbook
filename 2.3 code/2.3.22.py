n = int(input())
deck = list(range(n))

def faro(l):
    shuffle = l.copy()
    top, bottom = shuffle[n//2:], shuffle[:n//2]
    for i in range(n):
        if i % 2 == 0:
            shuffle[i] = bottom[i//2]
        elif i % 2 != 0:
            shuffle[i] = top[i//2]
    return shuffle

if n == 2:
    print(1)
else: 

    fn = faro(deck)
    c = 1

    while fn != deck:
        fn = faro(fn)
        c += 1

    print(c)