for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sol = []
    ans = 0
    for i in range(n):
        if a[i] < i+1:
            sol.append(i+1)
            if len(sol) > 1:
                l = 0
                u = len(sol)
                while l < u:
                    mid = (l+u)//2
                    if sol[mid] < a[i]:
                        l = mid + 1
                    else:
                        u = mid

                ans += len(sol[:l])

    print(ans)
