from bisect import bisect_left

for _ in range(int(input())):
    n, q = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    a = sorted(a, reverse=True)

    for i in range(1, n):
        a[i] = a[i]+a[i-1]

    for i in range(q):
        qi = int(input())

        left = bisect_left(a, qi)+1
        if left > n:
            print(-1)
        else:
            print(left)
