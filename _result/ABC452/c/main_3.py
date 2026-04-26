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

# candidatesを長さでグループ化
by_length = defaultdict(list)
for s in candidates:
    by_length[len(s)].append(s)

# Bにくる値をdictにする
can_place = defaultdict(set)
unique_keys = set(zip(A, B))
for a, b in unique_keys:
    for s in by_length[a]:
        can_place[a, b].add(s[b - 1])

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
