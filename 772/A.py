for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split(' ')))

    a_1 = a[0]
    for i in range(1, len(a), 1):
        a_1 = a_1 | a[i]

    print(a_1)
