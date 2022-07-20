
import math
for _ in range(int(input())):
    h, c, t = map(int, input().split())

    l = 1
    u = 10**7

    best = 10**7
    ans = 10**7

    if (h+c)/2 == t:
        print(2)
    elif h == t:
        print(1)
    elif c == t:
        print(2)
    else:
        while l+2 < u:
            inter = (l+u)//2
            if inter % 2 == 0:
                inter += 1
            a = (h*math.ceil(inter/2) + c*math.floor(inter/2))/inter
            if a >= t:
                l = inter
            else:
                u = inter

            if abs(a-t) < best:
                best = abs(a-t)
                ans = inter
            if a == t:
                break

        if abs(((h+c)/2)-t) <= best:
            print(2)
        elif abs(h-t) <= best:
            print(1)
        else:
            print(ans)
