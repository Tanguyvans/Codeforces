from bisect import bisect_left

n = int(input())

a = list(map(int, input().split(' ')))
a = sorted(a)

m = int(input())

for i in range(m):
    u = n
    l = 0
    c = int(input())
    while l < u:
        inter = (l+u)//2

        if c < a[inter]:
            u = inter
        else:
            l = inter + 1

    print(u)
