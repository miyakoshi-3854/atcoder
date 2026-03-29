n_employees, m_depts = map(int, input(), split())

current_bumon_result = [0] * (m_depts + 1)
future_bumon_result = [0] * (m_depts + 1)
for _ in range(n_employees):
    c, f = map(int, input().split())
    current_bumon_result[c] += 1
    future_bumon_result[f] += 1

for i in range(1, m_depts + 1):
    result = future_bumon_result[i] - current_bumon_result[i]
    print(result)
