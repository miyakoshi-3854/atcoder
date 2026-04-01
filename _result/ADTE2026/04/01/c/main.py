# 入力
N = int(input())
A = input().split(" ")
B = input().split(" ")

# 処理
Hit = 0
Blow = 0
for i, a in enumerate(A):
    for j, b in enumerate(B):
        if a == b and i == j:
            Hit += 1
        elif a == b:
            Blow += 1

print(Hit, Blow, sep="\n")