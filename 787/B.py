import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        imp = False
        flag = True
        for i in range(1, n):
            if a[i-1] >= a[i] and a[i-1] > 0:
                a[i-1] = math.floor(a[i-1]/2)
                flag = False
                ans += 1
                break
            elif a[i-1] == a[i] == 0:
                imp = True
                flag = True
                break

        if flag:
            break

    if imp:
        print(-1)
    else:
        print(ans)
