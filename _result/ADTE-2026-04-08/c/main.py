N, M = map(int, input().split())
S = [input() for _ in range(N)]

correct_count = 0
for i in range(N):
    for j in range(i + 1, N):
        is_valid_pair = True
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                is_valid_pair = False
                break
        if is_valid_pair:
            correct_count += 1

print(correct_count)
