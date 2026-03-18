# 直径Dの円の面積を求める問題
# 円の面積の求め方
# 半径 * 半径 * 円周率

# 必要なπだけインポートする
from math import pi

# 入力
D = int(input())

# 処理
# 直径Dから半径を求める
half: int = D / 2

result: int = half * half * pi

# 出力
print(result)
