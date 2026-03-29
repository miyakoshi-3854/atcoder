def count_per_bumon(assignments: list[int], m_depts: int) -> list[int]:
    result = [0] * (m_depts + 1)
    for dept in assignments:
        result[dept] += 1
    return result


n_employees, m_depts = map(int, input().split())

current_bumon = [0] * n_employees
future_bumon = [0] * n_employees
for i in range(n_employees):
    current_bumon[i], future_bumon[i] = map(int, input().split())


current_bumon_result = count_per_bumon(current_bumon, m_depts)
future_bumon_result = count_per_bumon(future_bumon, m_depts)

for i in range(1, m_depts + 1):
    result = future_bumon_result[i] - current_bumon_result[i]
    print(result)
