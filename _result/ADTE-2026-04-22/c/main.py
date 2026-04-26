"""
abc_255_b

条件
x, y は座標
a k に同じ強さの明かりを持たせる

思考
r を逆算する問題か？
x, yにいるN人の中から一番遠い間の距離を求める問題っぽい

でもどうやって二次元上の距離をコードで考えるんだ？
三平方の定理を使うのかな？

n * (n - 1) の組み合わせの中から一番おおきいもの

"""

n, k = map(int, input().split())
a = [int(_) for _ in input().split()]
x, y = [], []
for i in range(n):
    x, y = map(int, input().split())
