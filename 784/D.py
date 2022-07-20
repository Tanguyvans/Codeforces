for _ in range(int(input())):
    n = int(input())
    l = input()

    r = 0
    b = 0
    flag = True
    for i in l:
        if i == 'R':
            r = 1

        elif i == 'B':
            b = 1

        elif i == 'W' and r == b:
            r = 0
            b = 0

        elif i == 'W' and r != b:
            flag = False
            break

    if flag and r == b:
        print('YES')
    else:
        print('NO')
