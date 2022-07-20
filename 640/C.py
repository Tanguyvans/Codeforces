import math

for _ in range(int(input())):
    n, k = map(int, input().split(' '))

    l = 0
    u = 10**10

    while l < u:
        inter = (l+u) // 2

        if inter - int(math.floor(inter/n)) < k:
            l = inter + 1

        else:
            u = inter

    print(u)
