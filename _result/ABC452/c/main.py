from collections import defaultdict

# 入力
N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
M = int(input())
strings = []
for i in range(M):
    strings += input().split()

# Bにくる値をdictにする
can_place = defaultdict(set)
for i in range(N):
    for S in strings:
        if A[i] == len(S):
            can_place[A[i], B[i]].add(S[B[i] - 1])

# can_placeに当てはまるsが存在するか
for S in strings:
    if len(S) == N:
        for i in range(N):
            if S[i] not in can_place[(A[i], B[i])]:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
