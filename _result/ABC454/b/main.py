"""
条件
全員着ている服が違う
m種類の服を最低一枚誰かが着ているか
"""

n, m = map(int, input().split())
f = [int(f) for f in input().split()]

# 来ている服が違う
if len(f) == len(set(f)):
    print("Yes")
else:
    print("No")

# m種類の服を最低一枚着ているか
if len(set(f)) == m:
    print("Yes")
else:
    print("No")
