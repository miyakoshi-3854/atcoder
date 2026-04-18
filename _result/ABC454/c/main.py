"""
前提
n個のアイテム
m人の友達

条件
最初に持っているitem含めて、合計何種類のアイテムを手に入れたことがあるか

set(b) + 1したら答え出そう
→ 出なかった。

ちゃんと、アイテム所持数を管理する必要がありそう
dictで管理してみるか
→ 複雑にしなくていいはず
→→ dictであげる:もらうmapを作るべきだった
"""
from collections import defaultdict

_, friends = map(int, input().split())
exchanges = [list(map(int, input().split())) for _ in range(friends)]

trade_map = defaultdict(list)
for give, get in exchanges:
    trade_map[give].append(get)

collected = {1}
queue = [1]
for item in queue:
    for next_item in trade_map[item]:
        if next_item not in collected:
            collected.add(next_item)
            queue.append(next_item)

print(len(collected))