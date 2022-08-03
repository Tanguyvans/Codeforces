from re import M


import math

for _ in range(int(input())):
    n, h0, m0 = map(int, input().split())
    a0 = h0 * 60 + m0

    af = 24 * 60

    for i in range(n):
        h, m = map(int, input().split())

        ai = h * 60 + m

        if a0 <= ai:
            af = min(af, ai-a0)
        else:
            af = min(af, 24*60 - a0 + ai)

    print(math.floor(af/60), af % 60)
