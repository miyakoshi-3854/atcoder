n, s, m, l = map(int, input().split())

money = []
for i in range(18):
    for j in range(14):
        for k in range(10):
            egg = 6 * i + 8 * j + 12 * k
            total = s * i + m * j + l * k
            if egg >= n:
                money.append(total)

print(min(money))
