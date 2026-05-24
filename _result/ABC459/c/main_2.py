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
多分all()が終ってんだろうな

他にもうまくできることろあるかも

"""

n, q = map(int, input().split())

a = [0] * (n + 1)
c = [0] * (q + 1)
min = 0

for _ in range(q):
    t, x = map(int, input().split())

    if t == 1:
        a[x] += 1
        c[a[x]] += 1

        if c[a[x]] == n:
            min = a[x]

    if t == 2:
        if x + min > q:
            print(0)
        else:
            print(c[x + min])
