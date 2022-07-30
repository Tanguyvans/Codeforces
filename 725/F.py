import math
for _ in range(int(input())):
    l, r = map(int, input().split())

    ans = 0
    count = 0
    for i in range(9, -1, -1):
        ans += (math.floor(r/10**i) - math.floor(l/10**i))*(i+1) - count
        count += math.floor(r/10**i) - math.floor(l/10**i)

    print(ans)
