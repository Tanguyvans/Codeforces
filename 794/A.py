for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))
    flag = False
    for i in range(1, n):
        if a[i-1] != a[i]:
            flag = True
            break

    if flag:
        for i in range(n):
            if a[i] == (sum(a[:i]) + sum(a[i+1:]))/(n-1):
                flag = False
                break

    if flag:
        print('NO')
    else:
        print('YES')
