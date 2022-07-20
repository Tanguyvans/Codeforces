import math

for i in range(int(input())):
    k, n, a, b = map(int, input().split())

    l = 0
    u = k//b

    if n*b >= k:
        print(-1)
    else:
        while l <= u:
            inter = (l+u)//2
            if (inter*a)+(n-inter)*b < k:
                l = inter + 1
            else:
                u = inter - 1

        print(min(l, u, n))
