n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split(' '))

    if c-b == b-a:
        print('YES')
        continue

    m = (2*b-a)/c
    if (c * int(m)) - b == b-a and m > 0:
        print("YES")
        continue

    m = int((2*b-c)/a)
    if c-b == b-(a*int(m)) and m > 0:
        print("YES")
        continue

    m = int((a+c)/(2*b))
    if c-b*int(m) == b*int(m)-a and m > 0:
        print("YES")
        continue

    print('NO')
