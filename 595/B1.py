for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        sol = a[i]
        ans = 1
        while sol-1 != i:
            ans += 1
            sol = a[sol-1]

        print(ans, end=' ')

    print()
