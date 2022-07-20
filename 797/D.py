for _ in range(int(input())):
    n, k = map(int, input().split(' '))

    a = input()

    counter = 0
    for i in a[0:k]:
        if i == 'W':
            counter += 1
    ans = counter

    for i in range(1, n-k+1):
        if a[i-1] == 'W':
            counter -= 1
        if a[i+k-1] == 'W':
            counter += 1

        ans = min(ans, counter)

    print(ans)
