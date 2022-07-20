n = int(input())

x_1 = float('-inf')
h_1 = 0
ans = 0
for i in range(n):
    x, h = map(int, input().split(' '))

    if h_1 != 0 and h_1 < x-x_1:
        ans += 1
        if h < x - x_1 - h_1:
            ans += 1
            h_1 = 0
        else:
            h_1 = h

        x_1 = x

    elif x-h > x_1:
        ans += 1
        x_1 = x
        h_1 = 0
    else:
        h_1 = h
        x_1 = x

if h_1 != 0:
    ans += 1

print(ans)
