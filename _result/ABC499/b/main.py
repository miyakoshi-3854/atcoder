# B - Deconstruct Chocolate

# 入力
H, W, Q = map(int, input().split())

# Q回分、Q1, Q2を受け取る
query = [0] * Q
RorC = [0] * Q
for i in range(Q):
  query[i], RorC[i] = map(int, input().split())

# チョコレートの数
Chocolate = H * W

# 処理
for i in range(Q):
  if query[i] == 1:
    print(RorC[i] * W) # 行
    H -= RorC[i]
  elif query[i] == 2:
    print(RorC[i] * H) # 列
    W -= RorC[i]