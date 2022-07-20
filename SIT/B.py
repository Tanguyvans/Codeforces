x, n = map(int, input().split(' '))

ans = 0

for i in range(n):
    ans += x
    if (i+2) % 5 == 0 and i != 0:
        x -= 2
    else:
        x += 1

print(ans)
