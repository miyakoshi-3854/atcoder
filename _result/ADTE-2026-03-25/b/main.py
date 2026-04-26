start, end, current = map(int, input().split())

if start < end:
    print("Yes" if start <= current < end else "No")
else:
    print("Yes" if current >= start or current < end else "No")
