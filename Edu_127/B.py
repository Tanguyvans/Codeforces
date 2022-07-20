
import math

for _ in range(int(input())):

    n = int(input())

    a = list(map(int, input().split(' ')))

    if len(a) <= 2:
        print('YES')
    elif a[-1]-a[0] == 0 and len(a) > 3:
        print('NO')
    else:

        inter = math.ceil((a[-1]-a[0]+2)/len(a))

        flag = False
        for i in range(len(a)-1):
            if a[i+1] - a[i] > inter + 1 or a[i+1] - a[i] < inter - 1:
                flag = True

        if flag:
            print('NO')
        else:
            print('YES')
