import math

for _ in range(int(input())):
    n, x = map(int, input().split(' '))

    a = list(map(int, input().split(' ')))
    odd = 0
    even = 0

    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd == 0:
        print('No')
    else:
        ans = 1
        odd -= 1
        if x % 2 == 0:
            if even == 0:
                print('No')
            else:
                ans += 1
                even -= 1
                if ans + even + math.floor(odd/2)*2 >= x:
                    print('Yes')
                else:
                    print('No')
        else:
            if ans + even + math.floor(odd/2)*2 >= x:
                print('Yes')
            else:
                print('No')
