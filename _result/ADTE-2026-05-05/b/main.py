_ = int(input())
s = input()

T, A = 0, 0
for c in s:
    if c == "T":
        T += 1
    else:
        A += 1

if T == A and s[-1] == "T":
    print("A")
elif T == A and s[-1] == "A":
    print("T")
elif T < A:
    print("A")
else:
    print("T")
