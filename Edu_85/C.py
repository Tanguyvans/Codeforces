import io
import os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n = int(input())

    a = []
    b = []

    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    ans = 10**18
    sol = 0
    for i in range(n):
        mn = min(a[i], b[i-1])
        sol += a[i] - mn

        ans = min(ans, mn)

    print(sol + ans)
