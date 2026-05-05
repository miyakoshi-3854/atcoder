from collections import defaultdict

a = [int(_) for _ in input().split()]
d = defaultdict(int)

for n in a:
    d[n] += 1

count = 0
for n in d:
    count += d[n] // 2

print(count)
