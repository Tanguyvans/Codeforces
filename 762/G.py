from collections import deque as dq

for _ in range(int(input())):
    n, k = map(int, input().split())

    bombs = dict()

    l = 0
    u = 10**9
    for i in range(n):
        x, y, t = map(int, input().split())

        bombs[(x, y,)] = t

        l = min(l, t)
        u = max(u, t)

    while u > l:
        mid = (u+l)//2

        for key, val in bombs:
            d = dq()

            d.append(key)
