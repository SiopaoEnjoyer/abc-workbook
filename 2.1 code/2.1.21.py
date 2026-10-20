n = int(input())
l = [input() for _ in range(n)]
cvb = l[-1].split()[-1]
stren = ['Clubs', "Diamonds", "Hearts", "Spades"]
idx = stren.index(cvb)
alw = stren[:idx+1]
for i in l:
    if i.split()[-1] in alw:
        print(i)