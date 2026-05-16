"""
ABC458_c

条件
部分文字列を返す
奇数
中央がC

思考
これ尺取り法じゃない？
範囲を増やす条件
- 偶数の時
- C がない時

範囲を縮める条件
-

上記の考えじゃなくて、Cが来た時にあとどれだけ後ろに文字続いているかをカウントするのがいいか？

"""

s = input()

if "C" not in s:
    print(0)
    exit()

count = 0
for i in range(len(s)):
    if s[i] == "C":
        l = i
        r = len(s) - 1 - i
        count += min(l, r) + 1

print(count)
