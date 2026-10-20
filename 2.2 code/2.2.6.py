n = int(input())
c = [input() for _ in range(n)]
h = 0
red = ["Diamonds", "Hearts"]
black = ["Spades", "Clubs"]

for i in range(n):
    suit1 = c[i].split(" ")[-1]
    
    if i == 0:
        suit2 = c[i + 1].split(" ")[-1] if n > 1 else ""
        s1s2_red = suit1 in red and suit2 in red
        s1s2_black = suit1 in black and suit2 in black
        if s1s2_red or s1s2_black:
            h += 1

    elif i == n - 1:
        suit3 = c[i - 1].split(" ")[-1]
        s1s3_red = suit1 in red and suit3 in red
        s1s3_black = suit1 in black and suit3 in black
        if s1s3_red or s1s3_black:
            h += 1

    else:
        suit2 = c[i + 1].split(" ")[-1]
        suit3 = c[i - 1].split(" ")[-1]
        s1s2_red = suit1 in red and suit2 in red
        s1s2_black = suit1 in black and suit2 in black
        s1s3_red = suit1 in red and suit3 in red
        s1s3_black = suit1 in black and suit3 in black

        if (s1s2_red and s1s3_red) or (s1s2_black and s1s3_black):
            continue
        elif (s1s2_red and not s1s3_red) or (not s1s2_red and s1s3_red):
            h += 1
        elif (s1s2_black and not s1s3_black) or (not s1s2_black and s1s3_black):
            h += 1

print(h)