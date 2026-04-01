a, b = map(int, input().split())

# aがつながっている線を特定
line_1 = a * 2
line_2 = a * 2 + 1

if b == line_1 or b == line_2:
    print("Yes")
else:
    print("No")