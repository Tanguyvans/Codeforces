for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n % 2, n, 2):
        if a[i] > a[i+1]:
            mid = a[i]
            a[i] = a[i+1]
            a[i+1] = mid

    if a == sorted(a):
        print('YES')
    else:
        print('NO')
