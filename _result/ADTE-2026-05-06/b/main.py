h, w = map(int, input().split())
r, c = map(int, input().split())

h_l = []
for i in range(1, h + 1):
    h_l.append(i)
w_l = []
for i in range(1, w + 1):
    w_l.append(i)

count = 0
if r + 1 in h_l:
    count += 1
if r - 1 in h_l:
    count += 1
if c + 1 in w_l:
    count += 1
if c - 1 in w_l:
    count += 1

print(count)
