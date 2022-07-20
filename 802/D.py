import math

n = int(input())
a = list(map(int, input().split()))

sa = sum(a)
sol = [0 for i in range(n)]
s = 0
bf = 0
for i in range(n):
    s += a[i]
    sol[i] = max(math.ceil(s/(i+1)), math.ceil(sa/(i+1)), bf)
    bf = max(bf, math.ceil(s/(i+1)))

q = int(input())

for i in range(q):
    t = int(input())
    l = 0
    u = n
    if t < sol[-1]:
        print(-1)
    else:
        # print(sol)
        while l < u:
            inter = (l+u)//2

            if sol[inter] > t:
                l = inter + 1
            else:
                u = inter

        print(l+1)
