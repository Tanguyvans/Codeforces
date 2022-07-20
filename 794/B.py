for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split(' ')))

    ans = 0
    pas = False
    for i in range(1, n):

        if pas:
            pas = False
            continue
        if p[i-1] > p[i]:
            ans += 1
            pas = True

    print(ans)
