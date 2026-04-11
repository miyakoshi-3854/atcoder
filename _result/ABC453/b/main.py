unused, diff = map(int, input().split())
times = [int(i) for i in input().split()]

last_time = times[0]
for i, time in enumerate(times):
    if i == 0:
        print(i, time)
        continue

    if diff <= abs(last_time - time):
        print(i, time)
        last_time = times[i]
