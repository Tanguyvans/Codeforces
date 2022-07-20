import math

for _ in range(int(input())):
    n = int(input())

    h = list(map(int, input().split(' ')))
    max_h = max(h)

    odd0 = 0
    odd1 = 0
    even0 = 0
    even1 = 0
    l = 0
    u = 0
    for hi in h:
        diff = max_h-hi
        l += diff//2
        u += diff * 2

        if diff % 2 == 0:
            even0 += diff/2
            even1 += diff/2
            odd1 += 1
        else:
            odd0 += 1
            even0 += int((diff-1)/2)
            even1 += int((diff+1)/2)

    while l <= u:

        inter = int((l+u)/2)
        if (math.ceil(inter/2) >= odd0 and (math.floor(inter/2)*2+math.ceil(inter/2)-odd0) >= even0*2) or (math.ceil(inter/2) >= odd1 and (math.floor(inter/2)*2+math.ceil(inter/2)-odd1) >= even1*2):
            u = inter-1
        else:
            l = inter+1

    print(l)
