s = input()

l = -1
for i, c in enumerate(s):
    if c == "a":
        l = i + 1

print(l)
