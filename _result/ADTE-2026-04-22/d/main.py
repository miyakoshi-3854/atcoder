_, lowest = map(int, input().split())
scores = [int(_) for _ in input().split()]

count = 0
for score in scores:
    if score < lowest:
        count += 1

print(count)