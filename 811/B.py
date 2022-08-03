for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = set()
    ans = 0

    for i in range(n-1, -1, -1):
        if a[i] not in d:
            d.add(a[i])
        else:
            ans = i+1
            break

    print(ans)
