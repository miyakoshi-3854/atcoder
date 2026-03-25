N = int(input())

cost = [[0] * N for _ in range(N)]

for i in range(N - 1):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        cost[i][i + j + 1] = row[j]
        cost[i + j + 1][i] = row[j]

for a in range(N):
    for b in range(a + 1, N):
        for cost in range(b + 1, N):
            if cost[a][b] + cost[b][c] < cost[a][c]:
                print("Yes")
                exit()

print("No")
