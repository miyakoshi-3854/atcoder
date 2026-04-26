from collections import defaultdict

# 入力
N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
M = int(input())
candidates = []
for _ in range(M):
    candidates.extend(input().split())

# Bにくる値をdictにする
can_place = defaultdict(set)
for i in range(N):
    for s in candidates:
        if A[i] == len(s):
            can_place[A[i], B[i]].add(s[B[i] - 1])

# can_placeに当てはまるsが存在するか
for s in candidates:
    if len(s) == N:
        for i in range(N):
            if s[i] not in can_place[(A[i], B[i])]:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
