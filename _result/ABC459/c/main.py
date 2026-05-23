"""
ABC_c

条件
n列のマスがある

q1: n個のマス全てに1つ以上あったらテトリスのように消化する
q2: y個以上の数字がいくつあるか集計

q[i][0] == 1 なら q1
q[i][0] == 2 なら q2
q[i][1] は指定の数字

思考
テトリスみたいな感じ

dictで先に、n個の列分の数字を初期化したい。
dict設計
key: n番目, val: ブロック数 (初期値: 0)

注意
急にブロックを3個とか追加するときがあるなら、
whileで今のn列の状態を確認して、消化するかしないかを決める必要がある


うわーーーTLEだーーーー

"""

num, query = map(int, input().split())
qs = [list(map(int, input().split())) for _ in range(query)]

d = {}
for n in range(1, num + 1):
    d[n] = 0

for q in qs:
    if q[0] == 1:
        d[q[1]] += 1
        if all(v >= 1 for v in d.values()):
            for k in d:
                d[k] -= 1
    else:
        count = 0
        for v in d.values():
            if v >= q[1]:
                count += 1
        print(count)
