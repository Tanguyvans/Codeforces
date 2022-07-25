import math

color = list(map(int, input().split()))
ans = 0

while True:
    v_1 = 0
    p_1 = -1
    for i in range(3):
        if color[i] >= v_1:
            v_1 = color[i]
            p_1 = i
    v_2 = 0
    p_2 = -1
    for i in range(3):
        if i == p_1:
            if color[i]//2 >= v_2:
                v_2 = math.floor(color[i]/2)
                p_2 = i
        elif color[i] >= v_2:
            v_2 = color[i]
            p_2 = i

    v_3 = 0
    p_3 = -1
    for i in range(3):
        if i == p_1 == p_2:
            continue
        elif i == p_1:
            if color[i]//2 >= v_3:
                v_3 = math.floor(color[i]//2)
                p_3 = i
        elif i == p_2:
            if color[i]//2 >= v_3:
                v_3 = math.floor(color[i]//2)
                p_3 = i
        elif color[i] >= v_3:
            v_3 = color[i]
            p_3 = i

    prev = ans
    if p_1 != p_2 and p_2 != p_3 and p_1 != p_3:
        nb = v_1 - v_3 - 1
        ans += nb
        for i in range(3):
            color[i] -= nb

    else:
        nb = v_3
        ans += nb
        for i in [p_1, p_2, p_3]:
            color[i] -= nb

    print(color)

    if prev == ans:
        break


print(ans)
