"""
ABC420_b

条件
その時の回数で1, 0の少ない方に投票していた方に1点加算する

思考
matrixの縦横反転
二重forでひとつづつ見ていく
1, 0どっちが多いか集計、どちらに加算するか決定
dictでどっちにいれているのか管理


"""

n, m = map(int, input().split())
s = [input() for i in range(n)]

trans = [list(row) for row in zip(*s)]

count = [0] * n
for i in range(m):
    zero, one = 0, 0
    for j, vote in enumerate(trans[i]):
        if vote == "0":
            zero += 1
        else:
            one += 1

    if zero == 0 or one == 0:
        for j in range(n):
            count[j] += 1
        continue
    elif zero < one:
        minority = "0"
    else:
        minority = "1"

    for j, vote in enumerate(trans[i]):
        if vote == minority:
            count[j] += 1

max_score = max(count)
result = []
for j, score in enumerate(count):
    if score == max_score:
        result.append(j + 1)
print(*result)
