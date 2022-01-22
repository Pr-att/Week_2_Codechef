for _ in range(int(input())):
    data = list(map(int, input().split()))
    if data[2] * data[4] <= data[0] and data[3] * data[4] <= data[1]:
        print("YES")
    else:
        print('NO')