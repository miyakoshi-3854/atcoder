A, B = map(int, input().split())

m_diff = abs(A - B)
e_diff = 1
if m_diff == 0:
    print(1)
else:
    for _ in range(m_diff):
        e_diff *= 32
    print(e_diff)