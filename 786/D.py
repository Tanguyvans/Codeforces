for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))

    aa = []
    ab = []

    if len(a) <= 2:
        print('YES')
        continue

    for i in range(len(a)):
        if i % 2 == 0:
            aa.append(a[i])
        else:
            ab.append(a[i])

    if aa == sorted(aa) and ab == sorted(ab):
        flag = False

        if len(aa) > len(ab) and aa[0] > ab[0]:
            flag = True

        for i in range(len(ab)):

            if i > 0:
                if aa[i] < ab[i-1]:
                    flag = True
                    break
                if ab[i] < aa[i-1]:
                    flag = True
                    break

        if flag:
            print('NO')
        else:
            print('YES')

    else:
        print('NO')
