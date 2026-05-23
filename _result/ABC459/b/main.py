n = int(input())
ss = list(input().split())
res = []

for s in ss:
    c = s[0]
    if c == "a" or c == "b" or c == "c":
        res.append("2")
    if c == "d" or c == "e" or c == "f":
        res.append("3")
    if c == "g" or c == "h" or c == "i":
        res.append("4")
    if c == "j" or c == "k" or c == "l":
        res.append("5")
    if c == "m" or c == "n" or c == "o":
        res.append("6")
    if c == "p" or c == "q" or c == "r" or c == "s":
        res.append("7")
    if c == "t" or c == "u" or c == "v":
        res.append("8")
    if c == "w" or c == "x" or c == "y" or c == "z":
        res.append("9")

print("".join(res))
