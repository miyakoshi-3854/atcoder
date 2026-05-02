A = [list(map(int, input().split())) for _ in range(3)]

TARGET = {4, 5, 6}

count = 0
for x in A[0]:
    if x not in TARGET:
        continue
    for y in A[1]:
        if y not in TARGET:
            continue
        for z in A[2]:
            if {x, y, z} == TARGET:
                count += 1

result = count / 216
print(result)
