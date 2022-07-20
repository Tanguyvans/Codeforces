n = int(input())

x = 0
y = 0
z = 0

for i in range(n):
    xa, ya, za = map(int, input().split())

    x += xa
    y += ya
    z += za

if x == y == z == 0:
    print('YES')
else:
    print('NO')
