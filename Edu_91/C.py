import math

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a = sorted(a, reverse=True)

    b = [math.ceil(x/ai) for ai in a]
    no_team = 0
    ans = 0
    for i in range(n):
        no_team += 1

        if b[i] <= no_team:
            ans += 1
            no_team -= b[i]

    print(ans)
