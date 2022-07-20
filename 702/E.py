for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))
    aa = [[a[i], i] for i in range(n)]
    aa = sorted(aa, key=lambda aa: [aa[0]], reverse=True)
    s = sum(a)

    ind = 0
    for i in range(n):
        s -= aa[i][0]
        if s < aa[i][0]:
            ind = i
            break

    print(ind+1)
    aa = sorted(aa[:ind+1], key=lambda aa: [aa[1]])
    for ai in aa:
        print(ai[1]+1, end=' ')
    print('')
