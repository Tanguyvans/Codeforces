for _ in range(int(input())):

    l, r, k = map(int, input().split(' '))

    if l == 1 and r == 1:
        print('NO')
        continue
    if l == r:
        print('YES')
        continue

    if l % 2 == 0:
        if k >= (r-l)/2:
            print('YES')
        else:
            print('NO')

    else:
        if k >= (r-l+1)/2:
            print('YES')
        else:
            print('NO')
