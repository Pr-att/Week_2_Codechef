for i in range(int(input())):
    count = 0
    a = input().split()
    b = list(map(int, input().split()))
    print(b)
    c = [i + int(a[1]) for i in b]
    print(c)
    for _ in c:
        if _ % 7 == 0:
            count += 1
    print(count)
