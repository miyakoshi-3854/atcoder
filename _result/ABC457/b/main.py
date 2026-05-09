n = int(input())
a = [input().split() for _ in range(n)]
x, y = map(int, input().split())

print(a[x - 1][y])
