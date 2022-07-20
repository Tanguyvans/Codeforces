import math

r, x1, y1, x2, y2 = map(int, input().split(' '))

d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

ans = math.ceil(d/(r*2))

print(int(ans))
