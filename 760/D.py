import math

for _ in range(int(input())):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)

    ans = 0
    for i in range(n):
        if i < k:
            ans += int(math.floor(a[i+k]/a[i]))

        elif i >= 2*k:
            ans += a[i]

    print(ans)
