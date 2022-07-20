import math

for _ in range(int(input())):

    n = int(input())

    mid = n/3

    h2 = math.ceil(mid) + 1
    h3 = math.floor(mid) - 1

    h1 = n-h2-h3

    print(int(h1), int(h2), int(h3))
