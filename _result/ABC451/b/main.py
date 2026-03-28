# 入力
shain, bumon = map(int, input().split())

current_bumon = [0] * shain
feture_bumon = [0] * shain
for i in range(shain):
    current_bumon[i], feture_bumon[i] = map(int, input().split())

# 現在の部門数を数える
current_bumon_result = [0] * (bumon + 1)
for i in range(1, bumon + 1):
    count = 0
    for j in range(shain):
        if current_bumon[j] == i:
            count += 1
    current_bumon_result[i] = count

# 来年の部門数を数える
feture_bumon_result = [0] * (bumon + 1)
for i in range(1, bumon + 1):
    count = 0
    for j in range(shain):
        if feture_bumon[j] == i:
            count += 1
    feture_bumon_result[i] = count

# 来年 - 現在をして結果を出力
for i in range(1, bumon + 1):
    result = feture_bumon_result[i] - current_bumon_result[i]
    print(result)
