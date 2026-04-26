N = int(input())

s = ""

while N >= 1:
    s += str(N)

    if N > 1:
        s += ","

    N -= 1

print(s)
