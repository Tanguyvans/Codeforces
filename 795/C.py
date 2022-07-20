for _ in range(int(input())):
    n, k = map(int, input().split(' '))

    a = input()
    a = [int(i) for i in a]

    a0 = -1
    ones = 0
    an = -2
    for i in range(n):
        if a[i] == 1:
            if a0 == -1:
                a0 = i

            ones += 1
            an = i

    ans = 11 * ones

    if an == a0:
        if an == n-1:
            ans -= 10
        elif k >= n-1-an:
            ans -= 10
        elif an == 0:
            ans -= 1
        elif k >= an:
            ans -= 1
    else:
        if an != -2:
            if k >= n-1-an:
                k -= n-an-1
                ans -= 10
        if a0 != -1:
            if k >= a0:
                ans -= 1

    print(ans)
