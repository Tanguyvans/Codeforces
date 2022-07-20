n = int(input())
al = list(map(int, input().split(' ')))
val = 32768

for a in al:
    ans = 20
    for i in range(a, a+15):
        op = i - a

        while i % (32768) != 0 and op < 15:
            i *= 2
            i = i % 32768
            op += 1

        ans = min(ans, op)
    print(ans, end=' ')
