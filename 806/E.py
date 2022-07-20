import math
for _ in range(int(input())):
    n = int(input())
    a = [list(input()) for i in range(n)]

    ans = 0
    for i in range(int(math.floor(n/2))):
        for j in range(int(math.ceil(n/2))):
            #print('i', 'j', a[i][j], a[j][-1-i], a[-1-i][-1-j], a[-1-j][i])
            a1 = 4-int(a[i][j])-int(a[j][-1-i]) - \
                int(a[-1-i][-1-j])-int(a[-1-j][i])
            a2 = int(a[i][j])+int(a[j][-1-i]) + \
                int(a[-1-i][-1-j])+int(a[-1-j][i])

            ans += min(a1, a2)

    print(ans)
