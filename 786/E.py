import math

n = int(input())
a = list(map(int, input().split()))

ans = 1000000000

min_nb = 1000000000
for i in range(1, len(a)):
    if i == 1:
        ans = min(
            ans, max(math.ceil(a[i-1]/2), math.ceil((a[i-1]+a[i])/3), math.ceil(a[i]/2)))
        min_nb = min(min_nb, a[i-1])

    else:
        # i-1 , i
        ans = min(
            ans, max(math.ceil(a[i-1]/2), math.ceil((a[i-1]+a[i])/3), math.ceil(a[i]/2)))

        # i-2 , i
        ans = min(ans, max(a[i-2], a[i]), min(a[i-2],
                  a[i])+math.ceil(abs(a[i-2]-a[i])/2))
        # min i, i
        ans = min(ans, math.ceil(min_nb/2) + math.ceil(a[i]/2))

        min_nb = min(min_nb, a[i-1])

print(ans)
