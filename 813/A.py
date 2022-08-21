for _ in range(int(input())):
    n, k = map(int, input().split())

    p = list(map(int, input().split()))

    ans = 0
    pk = sorted(p[:k])
    for i in range(k):
        if i+1 not in pk:
            ans += 1

    print(ans)
