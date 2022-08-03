for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    a = [int(i) for i in a]
    b = input()
    b = [int(i) for i in b]

    if all(b[i] == a[n-m+i] for i in range(1, m)) and b[0] in a[:n-m+1]:
        print('YES')
    else:
        print('NO')
