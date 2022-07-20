for _ in range(int(input())):
    a = list(map(int, input().split()))

    a0 = a[0]
    ans = 0
    for i in range(1, len(a)):
        if a0 < a[i]:
            ans += 1

    print(ans)
