s = input()
if "." not in s:
    print("*"*len(s))
else:
    p = s.index(".")
    sentence = "*"*p + s[p:]
    print(sentence)