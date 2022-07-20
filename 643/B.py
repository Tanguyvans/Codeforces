for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    a = sorted(a)

    ans = 0

    group = 0
    for i in range(n):
        group += 1
        if group == a[i]:
            ans += 1
            group = 0

    print(ans)
