x1, y1, x2, y2 = map(int, input().split(' '))

flag = False
if x1 == x2:
    x3 = x1 + abs(y1-y2)
    y3 = min(y1, y2)

    x4 = x3
    y4 = max(y1, y2)

elif y1 == y2:
    y3 = y1 + abs(x1-x2)
    x3 = min(x1, x2)
    y4 = y3
    x4 = max(x1, x2)

elif (x2 > x1 and y2 > y1) or (x2 < x1 and y2 < y1):
    x3 = max(x1, x2)
    y3 = min(y1, y2)

    x4 = min(x1, x2)
    y4 = max(y1, y2)

    if abs(x3 - min(x1, x2)) != abs(y3 - max(y1, y2)):
        flag = True

else:
    x3 = max(x1, x2)
    y3 = max(y1, y2)

    x4 = min(x1, x2)
    y4 = min(y1, y2)

    if abs(x3 - min(x1, x2)) != abs(y3 - min(y1, y2)):
        flag = True

if flag:
    print(-1)
else:
    print(x3, y3, x4, y4)
