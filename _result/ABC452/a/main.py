gosekku_M = (
    1,
    3,
    5,
    7,
    9,
)
gosekku_D = (
    3,
    5,
    7,
    9,
)

M, D = map(int, input().split())

if M in gosekku_M and D in gosekku_D:
    print("Yes")
else:
    print("No")