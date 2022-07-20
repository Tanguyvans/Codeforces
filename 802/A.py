for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    ans += (m*(m+1))//2

    ans += m*(n*(n+1))//2 - m

    print(ans)
