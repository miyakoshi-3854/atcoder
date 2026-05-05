x = input()

result = []
zero_stack = []

x = list(x)
x.sort()
for n in x:
    if int(n) == 0:
        zero_stack.append(0)
        continue
    if int(n) != 0:
        result.append(n)
        while zero_stack:
            result.append(zero_stack.pop())

print("".join(map(str, result)))
