import math

for _ in range(int(input())):
    n, x = map(int, input().split(' '))

    a = list(map(int, input().split(' ')))
    a = sorted(a)

    som = 0
    size = 1
    ans = 0
    for i in a:
        d = math.floor(((x-som-i)/size)+1)
        if d <= 0:
            break
        ans += d
        size += 1
        som += i

    print(ans)
