for _ in range(int(input())):
    c_d = list(map(int, input().split()))
    day_1 = list(map(int, input().split()))
    day_2 = list(map(int, input().split()))
    if sum(day_1) >= 150:
        new_day_1 = sum(day_1) + c_d[0]
    else:
        new_day_1 = sum(day_1)
    if sum(day_2) >= 150:
        new_day_2 = sum(day_2) + c_d[0]
    else:
        new_day_2 = sum(day_2)

    if new_day_2 + new_day_1 > sum(day_1) + sum(day_2) + c_d[1]:
        print('YES')
    else:
        print('NO')
