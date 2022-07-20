for _ in range(int(input())):

    n = int(input())

    a = list(map(int, input().split(' ')))

    min_a = min(a)

    ans = 0
    for ai in a:

        ans += ai - min_a

    print(ans)
