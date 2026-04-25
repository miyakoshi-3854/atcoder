"""
ABC455_c

条件
出現する数字を記憶
0に置き換え * k回
一番小さくなる組み合わせを探す

思考
dictを使って出現した回数、出現した数をvalue部分に足す
dictをvalueで並べ替え
dictをk回0で書き換える

注意
python 3.11はdefaultdictをimportしないと使えない

"""
from collections import defaultdict

# 入力
_, times = map(int, input().split())
nums = [int(n) for n in input().split()]

result = 0

# 数字処理
nums_dict = defaultdict(int)
for n in nums:
    nums_dict[n] += n
nums_dict = dict(sorted(nums_dict.items(), key=lambda x: x[1], reverse=True))

# 書き換え処理
for i, key in enumerate(nums_dict.keys()):
    if i > times or i == times:
        break
    nums_dict[key] = 0

# 足す処理
for n in nums_dict.values():
    result += n

print(result)