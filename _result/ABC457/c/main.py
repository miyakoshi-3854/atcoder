"""
ABC457_c

愚直にやったらTLEになった。
どうやって最適化するんだろう？


"""

n, k = map(int, input().split())
a = [list(map(int, input().split()))[1:] for _ in range(n)]
c = list(map(int, input().split()))

# b = []
# for i in range(n):
#     for j in range(c[i]):
#         b += a[i][1:]
# print(b[k - 1])

for i in range(n):
    L = len(a[i])  # len() で取れる
    total = L * c[i]
    if k > total:
        k -= total
    else:
        pos = (k - 1) % L
        print(a[i][pos])  # [1 + pos] → [pos] になる
        break
