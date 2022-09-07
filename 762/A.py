for _ in range(int(input())):
    a = list(input())

    if a[:len(a)//2] == a[len(a)//2:]:
        print('YES')
    else:
        print('NO')
