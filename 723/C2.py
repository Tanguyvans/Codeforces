from heapq import heappop, heappush

n = int(input())

a = list(map(int, input().split()))

hp = 0
ans = 0
pt = list()

for i in range(n):
    if a[i] > 0:
        hp += a[i]
        ans += 1

    elif hp + a[i] >= 0:
        hp += a[i]
        ans += 1
        heappush(pt, a[i])
    elif pt:
        a1 = heappop(pt)
        if a1 < a[i]:
            hp = hp - a1 + a[i]
            heappush(pt, a[i])
        else:
            heappush(pt, a1)

print(ans)
