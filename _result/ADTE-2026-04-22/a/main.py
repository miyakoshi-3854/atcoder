_, c1, c2 = input().split()
s = input()

result = []

for c in s:
    if c != c1:
        result.append(c2)
    else:
        result.append(c1)

print("".join(result))
